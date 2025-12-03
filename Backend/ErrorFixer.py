"""Error Fixing Tool for Jarvis - Analyzes and fixes Python errors"""
import re
import os
import sys
import traceback
from pathlib import Path


class ErrorFixer:
    """Analyzes Python errors and provides fixes"""
    
    def __init__(self):
        self.common_errors = {
            "ModuleNotFoundError": self._fix_module_not_found,
            "ImportError": self._fix_import_error,
            "SyntaxError": self._fix_syntax_error,
            "IndentationError": self._fix_indentation_error,
            "NameError": self._fix_name_error,
            "AttributeError": self._fix_attribute_error,
            "TypeError": self._fix_type_error,
            "ValueError": self._fix_value_error,
            "FileNotFoundError": self._fix_file_not_found,
            "KeyError": self._fix_key_error,
        }
    
    def analyze_error(self, error_text):
        """
        Analyze error text and provide solutions
        
        Args:
            error_text: The error message or traceback
            
        Returns:
            dict with error info and solutions
        """
        result = {
            "error_type": "Unknown",
            "error_message": "",
            "file": "",
            "line": 0,
            "solutions": [],
            "code_snippet": "",
            "fixed_code": ""
        }
        
        try:
            # Extract error type
            error_match = re.search(r'(\w+Error|\w+Exception):', error_text)
            if error_match:
                result["error_type"] = error_match.group(1)
            
            # Extract error message
            lines = error_text.strip().split('\n')
            if lines:
                result["error_message"] = lines[-1]
            
            # Extract file and line number
            file_match = re.search(r'File "([^"]+)", line (\d+)', error_text)
            if file_match:
                result["file"] = file_match.group(1)
                result["line"] = int(file_match.group(2))
            
            # Get solutions based on error type
            if result["error_type"] in self.common_errors:
                solutions = self.common_errors[result["error_type"]](error_text)
                result["solutions"] = solutions
            else:
                result["solutions"] = self._get_generic_solutions(error_text)
            
            # Try to get code snippet
            if result["file"] and result["line"]:
                result["code_snippet"] = self._get_code_snippet(
                    result["file"], 
                    result["line"]
                )
        
        except Exception as e:
            print(f"Error analyzing: {e}")
        
        return result
    
    def _fix_module_not_found(self, error_text):
        """Fix ModuleNotFoundError"""
        solutions = []
        
        # Extract module name
        module_match = re.search(r"No module named '([^']+)'", error_text)
        if module_match:
            module_name = module_match.group(1)
            
            solutions.append({
                "title": f"Install {module_name}",
                "command": f"pip install {module_name}",
                "description": f"Install the missing module using pip"
            })
            
            # Check for common module name variations
            common_packages = {
                "cv2": "opencv-python",
                "PIL": "Pillow",
                "sklearn": "scikit-learn",
                "yaml": "pyyaml",
            }
            
            if module_name in common_packages:
                actual_package = common_packages[module_name]
                solutions.append({
                    "title": f"Install correct package",
                    "command": f"pip install {actual_package}",
                    "description": f"The module '{module_name}' is part of '{actual_package}'"
                })
        
        solutions.append({
            "title": "Check virtual environment",
            "command": "pip list",
            "description": "Make sure you're in the correct virtual environment"
        })
        
        return solutions
    
    def _fix_import_error(self, error_text):
        """Fix ImportError"""
        solutions = []
        
        solutions.append({
            "title": "Reinstall package",
            "command": "pip install --upgrade --force-reinstall [package_name]",
            "description": "Reinstall the package to fix corrupted installation"
        })
        
        solutions.append({
            "title": "Check Python version",
            "command": "python --version",
            "description": "Some packages require specific Python versions"
        })
        
        return solutions
    
    def _fix_syntax_error(self, error_text):
        """Fix SyntaxError"""
        solutions = []
        
        if "invalid syntax" in error_text:
            solutions.append({
                "title": "Check for missing colons",
                "description": "Make sure if/for/while/def statements end with ':'"
            })
            
            solutions.append({
                "title": "Check for missing parentheses",
                "description": "Ensure all opening brackets have closing brackets"
            })
            
            solutions.append({
                "title": "Check for missing quotes",
                "description": "Make sure all strings are properly quoted"
            })
        
        if "EOL" in error_text or "EOF" in error_text:
            solutions.append({
                "title": "Unclosed string or bracket",
                "description": "You have an unclosed string, parenthesis, or bracket"
            })
        
        return solutions
    
    def _fix_indentation_error(self, error_text):
        """Fix IndentationError"""
        solutions = []
        
        solutions.append({
            "title": "Use consistent indentation",
            "description": "Use either 4 spaces or tabs, not both"
        })
        
        solutions.append({
            "title": "Check indentation level",
            "description": "Make sure code blocks are properly indented"
        })
        
        solutions.append({
            "title": "Auto-format code",
            "command": "python -m black your_file.py",
            "description": "Use Black formatter to fix indentation automatically"
        })
        
        return solutions
    
    def _fix_name_error(self, error_text):
        """Fix NameError"""
        solutions = []
        
        # Extract variable name
        var_match = re.search(r"name '([^']+)' is not defined", error_text)
        if var_match:
            var_name = var_match.group(1)
            
            solutions.append({
                "title": f"Define '{var_name}' before using it",
                "description": f"Make sure '{var_name}' is defined before this line"
            })
            
            solutions.append({
                "title": "Check for typos",
                "description": f"Verify the spelling of '{var_name}'"
            })
            
            solutions.append({
                "title": "Check variable scope",
                "description": f"'{var_name}' might be defined in a different scope"
            })
        
        return solutions
    
    def _fix_attribute_error(self, error_text):
        """Fix AttributeError"""
        solutions = []
        
        solutions.append({
            "title": "Check object type",
            "description": "Make sure you're calling the method on the correct object type"
        })
        
        solutions.append({
            "title": "Check for None",
            "description": "The object might be None. Add a check: if obj is not None:"
        })
        
        solutions.append({
            "title": "Check spelling",
            "description": "Verify the attribute/method name is spelled correctly"
        })
        
        return solutions
    
    def _fix_type_error(self, error_text):
        """Fix TypeError"""
        solutions = []
        
        if "unsupported operand type" in error_text:
            solutions.append({
                "title": "Convert types",
                "description": "Convert variables to compatible types (e.g., str to int)"
            })
        
        if "missing" in error_text and "required positional argument" in error_text:
            solutions.append({
                "title": "Add missing arguments",
                "description": "The function call is missing required arguments"
            })
        
        if "takes" in error_text and "positional argument" in error_text:
            solutions.append({
                "title": "Check function arguments",
                "description": "You're passing wrong number of arguments to the function"
            })
        
        return solutions
    
    def _fix_value_error(self, error_text):
        """Fix ValueError"""
        solutions = []
        
        if "invalid literal" in error_text:
            solutions.append({
                "title": "Validate input",
                "description": "Check if the input can be converted to the target type"
            })
            
            solutions.append({
                "title": "Add try-except",
                "code": "try:\n    value = int(input_str)\nexcept ValueError:\n    print('Invalid input')",
                "description": "Handle conversion errors gracefully"
            })
        
        return solutions
    
    def _fix_file_not_found(self, error_text):
        """Fix FileNotFoundError"""
        solutions = []
        
        # Extract filename
        file_match = re.search(r"\[Errno 2\] No such file or directory: '([^']+)'", error_text)
        if file_match:
            filename = file_match.group(1)
            
            solutions.append({
                "title": "Check file path",
                "description": f"Verify that '{filename}' exists at the specified location"
            })
            
            solutions.append({
                "title": "Use absolute path",
                "code": f"import os\nfile_path = os.path.abspath('{filename}')",
                "description": "Use absolute path instead of relative path"
            })
            
            solutions.append({
                "title": "Create file if missing",
                "code": f"if not os.path.exists('{filename}'):\n    open('{filename}', 'w').close()",
                "description": "Create the file if it doesn't exist"
            })
        
        return solutions
    
    def _fix_key_error(self, error_text):
        """Fix KeyError"""
        solutions = []
        
        solutions.append({
            "title": "Use .get() method",
            "code": "value = dictionary.get('key', default_value)",
            "description": "Use .get() to avoid KeyError"
        })
        
        solutions.append({
            "title": "Check if key exists",
            "code": "if 'key' in dictionary:\n    value = dictionary['key']",
            "description": "Check if key exists before accessing"
        })
        
        return solutions
    
    def _get_generic_solutions(self, error_text):
        """Get generic solutions for unknown errors"""
        solutions = []
        
        solutions.append({
            "title": "Read the error message carefully",
            "description": "The error message usually tells you what went wrong"
        })
        
        solutions.append({
            "title": "Check the line number",
            "description": "Look at the line mentioned in the error traceback"
        })
        
        solutions.append({
            "title": "Search online",
            "description": "Copy the error message and search on Google or Stack Overflow"
        })
        
        return solutions
    
    def _get_code_snippet(self, filepath, line_number, context=3):
        """Get code snippet around the error line"""
        try:
            if not os.path.exists(filepath):
                return ""
            
            with open(filepath, 'r', encoding='utf-8') as f:
                lines = f.readlines()
            
            start = max(0, line_number - context - 1)
            end = min(len(lines), line_number + context)
            
            snippet = ""
            for i in range(start, end):
                marker = ">>> " if i == line_number - 1 else "    "
                snippet += f"{marker}{i+1:4d} | {lines[i]}"
            
            return snippet
        
        except Exception as e:
            return f"Could not read file: {e}"
    
    def format_solution(self, analysis):
        """Format the analysis result as readable text"""
        output = []
        
        output.append("="*60)
        output.append("ERROR ANALYSIS")
        output.append("="*60)
        
        output.append(f"\n❌ Error Type: {analysis['error_type']}")
        output.append(f"📝 Message: {analysis['error_message']}")
        
        if analysis['file']:
            output.append(f"📁 File: {analysis['file']}")
            output.append(f"📍 Line: {analysis['line']}")
        
        if analysis['code_snippet']:
            output.append(f"\n📄 Code Snippet:")
            output.append(analysis['code_snippet'])
        
        if analysis['solutions']:
            output.append(f"\n💡 Solutions:")
            for i, solution in enumerate(analysis['solutions'], 1):
                output.append(f"\n{i}. {solution['title']}")
                output.append(f"   {solution['description']}")
                
                if 'command' in solution:
                    output.append(f"   Command: {solution['command']}")
                
                if 'code' in solution:
                    output.append(f"   Code:")
                    for line in solution['code'].split('\n'):
                        output.append(f"      {line}")
        
        output.append("\n" + "="*60)
        
        return "\n".join(output)


def analyze_error_from_file(filepath):
    """Analyze error from a log file"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            error_text = f.read()
        
        fixer = ErrorFixer()
        analysis = fixer.analyze_error(error_text)
        return fixer.format_solution(analysis)
    
    except Exception as e:
        return f"Error reading file: {e}"


def analyze_error_from_text(error_text):
    """Analyze error from text"""
    fixer = ErrorFixer()
    analysis = fixer.analyze_error(error_text)
    return fixer.format_solution(analysis)


# Test function
if __name__ == "__main__":
    print("="*60)
    print("JARVIS ERROR FIXER - TEST")
    print("="*60)
    
    # Test cases
    test_errors = [
        "ModuleNotFoundError: No module named 'cv2'",
        "NameError: name 'x' is not defined",
        "IndentationError: unexpected indent",
        "FileNotFoundError: [Errno 2] No such file or directory: 'data.txt'",
    ]
    
    fixer = ErrorFixer()
    
    for error in test_errors:
        print(f"\nTesting: {error}")
        result = analyze_error_from_text(error)
        print(result)
        print()
