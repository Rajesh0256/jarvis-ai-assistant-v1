from pathlib import Path

test_folder = Path.home() / 'Desktop' / 'test_select_folder'
test_folder.mkdir(exist_ok=True)

for i in range(5):
    (test_folder / f'test_file_{i}.txt').write_text(f'Test file {i}')

print(f'Created test folder with 5 files: {test_folder}')
