"""
Religion and History Knowledge Module for Jarvis AI
Comprehensive information about world religions and historical events
"""

from groq import Groq
from dotenv import dotenv_values
import json

env_vars = dotenv_values(".env")
GroqAPIKey = env_vars.get("GroqAPIKey", "")
Username = env_vars.get("Username", "User")
Assistantname = env_vars.get("Assistantname", "Jarvis")

if not GroqAPIKey:
    print("Warning: GroqAPIKey not found in .env file")
    GroqAPIKey = "dummy_key"

client = Groq(api_key=GroqAPIKey)

# Comprehensive Religion Knowledge Base
RELIGION_KNOWLEDGE = """
MAJOR WORLD RELIGIONS:

1. CHRISTIANITY (2.4 billion followers)
   - Founded: ~30 CE by Jesus Christ
   - Holy Book: Bible (Old Testament + New Testament)
   - Core Beliefs: Monotheistic, belief in Jesus as Son of God, salvation through faith
   - Major Branches: Catholic, Protestant, Orthodox
   - Key Practices: Prayer, church attendance, sacraments, baptism
   - Sacred Places: Jerusalem, Vatican City, Bethlehem

2. ISLAM (1.9 billion followers)
   - Founded: 610 CE by Prophet Muhammad
   - Holy Book: Quran (Qur'an)
   - Core Beliefs: Monotheistic (Allah), Five Pillars of Islam, prophets including Muhammad
   - Major Branches: Sunni (85-90%), Shia (10-15%)
   - Key Practices: Five daily prayers, fasting (Ramadan), Hajj pilgrimage, charity (Zakat)
   - Sacred Places: Mecca, Medina, Jerusalem (Al-Aqsa Mosque)

3. HINDUISM (1.2 billion followers)
   - Founded: ~1500 BCE (no single founder)
   - Holy Books: Vedas, Upanishads, Bhagavad Gita, Ramayana, Mahabharata
   - Core Beliefs: Dharma, Karma, Reincarnation, Moksha, multiple deities (Brahma, Vishnu, Shiva)
   - Key Practices: Puja (worship), yoga, meditation, festivals (Diwali, Holi)
   - Sacred Places: Varanasi, Ganges River, temples across India

4. BUDDHISM (520 million followers)
   - Founded: ~500 BCE by Siddhartha Gautama (Buddha)
   - Holy Books: Tripitaka, Sutras
   - Core Beliefs: Four Noble Truths, Eightfold Path, Nirvana, no permanent self
   - Major Branches: Theravada, Mahayana, Vajrayana (Tibetan)
   - Key Practices: Meditation, mindfulness, following precepts, monasticism
   - Sacred Places: Bodh Gaya, Lumbini, Sarnath

5. SIKHISM (30 million followers)
   - Founded: 1469 CE by Guru Nanak
   - Holy Book: Guru Granth Sahib
   - Core Beliefs: One God, equality of all humans, honest living, service
   - Key Practices: Prayer, community service (seva), wearing 5 Ks
   - Sacred Places: Golden Temple (Amritsar), Anandpur Sahib

6. JUDAISM (15 million followers)
   - Founded: ~2000 BCE with Abraham
   - Holy Book: Torah (first 5 books), Tanakh, Talmud
   - Core Beliefs: Monotheistic, covenant with God, chosen people, Messiah
   - Major Branches: Orthodox, Conservative, Reform
   - Key Practices: Sabbath, kosher diet, prayer, study of Torah
   - Sacred Places: Jerusalem (Western Wall), Temple Mount

7. JAINISM (4-5 million followers)
   - Founded: ~600 BCE by Mahavira
   - Holy Books: Agamas
   - Core Beliefs: Non-violence (Ahimsa), karma, liberation, no creator god
   - Key Practices: Strict vegetarianism, meditation, fasting, non-violence
   - Sacred Places: Palitana, Ranakpur, Shravanabelagola

8. ZOROASTRIANISM (200,000 followers)
   - Founded: ~1500 BCE by Zoroaster (Zarathustra)
   - Holy Book: Avesta
   - Core Beliefs: Dualism (good vs evil), one God (Ahura Mazda), free will
   - Key Practices: Fire worship, prayer, good thoughts/words/deeds
   - Sacred Places: Fire temples in Iran and India

9. SHINTO (4 million followers)
   - Founded: Ancient Japan (no founder)
   - Holy Books: Kojiki, Nihon Shoki
   - Core Beliefs: Kami (spirits), harmony with nature, ancestor worship
   - Key Practices: Shrine visits, festivals, purification rituals
   - Sacred Places: Ise Grand Shrine, Mount Fuji

10. TAOISM (12 million followers)
    - Founded: ~500 BCE by Laozi
    - Holy Book: Tao Te Ching
    - Core Beliefs: The Tao (the Way), harmony, balance (Yin-Yang), wu wei
    - Key Practices: Meditation, tai chi, feng shui, living simply
    - Sacred Places: Mount Tai, Wudang Mountains

11. CONFUCIANISM (6 million followers)
    - Founded: ~500 BCE by Confucius
    - Holy Books: Analects, Five Classics
    - Core Beliefs: Social harmony, filial piety, moral cultivation, respect
    - Key Practices: Rituals, ancestor veneration, education, ethics
    - Sacred Places: Temple of Confucius (Qufu)

12. BAHÁ'Í FAITH (5-8 million followers)
    - Founded: 1863 CE by Bahá'u'lláh
    - Holy Books: Kitáb-i-Aqdas, writings of Bahá'u'lláh
    - Core Beliefs: Unity of God, unity of religions, unity of humanity
    - Key Practices: Prayer, fasting, service to humanity
    - Sacred Places: Haifa (Israel), Acre

OTHER BELIEF SYSTEMS:
- Atheism/Agnosticism: No belief in deities or uncertain about existence
- Indigenous/Tribal Religions: Various native spiritual practices worldwide
- New Religious Movements: Scientology, Wicca, Rastafarianism, etc.
"""

# Comprehensive History Knowledge Base
HISTORY_KNOWLEDGE = """
MAJOR HISTORICAL PERIODS AND EVENTS:

ANCIENT HISTORY (3000 BCE - 500 CE):
- Mesopotamian Civilizations (Sumerians, Babylonians, Assyrians)
- Ancient Egypt (Pyramids, Pharaohs, 3100-30 BCE)
- Indus Valley Civilization (3300-1300 BCE)
- Ancient China (Dynasties: Shang, Zhou, Qin, Han)
- Ancient Greece (Democracy, Philosophy, Alexander the Great)
- Roman Empire (753 BCE - 476 CE)
- Persian Empire (550-330 BCE)
- Maurya Empire in India (322-185 BCE)

MEDIEVAL PERIOD (500 - 1500 CE):
- Byzantine Empire (330-1453 CE)
- Islamic Golden Age (8th-13th centuries)
- Crusades (1095-1291)
- Mongol Empire (1206-1368)
- Renaissance begins in Italy (14th century)
- Fall of Constantinople (1453)
- Printing Press invented by Gutenberg (1440)

EARLY MODERN PERIOD (1500 - 1800):
- Age of Exploration (Columbus 1492, Vasco da Gama 1498)
- Protestant Reformation (Martin Luther, 1517)
- Mughal Empire in India (1526-1857)
- Scientific Revolution (Copernicus, Galileo, Newton)
- English Civil War (1642-1651)
- American Revolution (1775-1783)
- French Revolution (1789-1799)

19TH CENTURY (1800 - 1900):
- Napoleonic Wars (1803-1815)
- Industrial Revolution
- American Civil War (1861-1865)
- Abolition of Slavery in various countries
- British Raj in India (1858-1947)
- Unification of Germany (1871)
- Scramble for Africa (colonization)
- Meiji Restoration in Japan (1868)

20TH CENTURY (1900 - 2000):
- World War I (1914-1918)
- Russian Revolution (1917)
- Great Depression (1929-1939)
- World War II (1939-1945)
- Holocaust (1941-1945)
- Atomic bombs on Hiroshima and Nagasaki (1945)
- Cold War (1947-1991)
- Indian Independence (1947)
- Chinese Communist Revolution (1949)
- Korean War (1950-1953)
- Vietnam War (1955-1975)
- Civil Rights Movement in USA (1950s-1960s)
- Moon Landing (1969)
- Fall of Berlin Wall (1989)
- Dissolution of Soviet Union (1991)

21ST CENTURY (2000 - Present):
- September 11 Attacks (2001)
- War in Afghanistan (2001-2021)
- Iraq War (2003-2011)
- Global Financial Crisis (2008)
- Arab Spring (2010-2012)
- COVID-19 Pandemic (2019-2023)
- Russia-Ukraine War (2022-present)

IMPORTANT HISTORICAL FIGURES:
- Alexander the Great (356-323 BCE)
- Julius Caesar (100-44 BCE)
- Ashoka the Great (304-232 BCE)
- Genghis Khan (1162-1227)
- Leonardo da Vinci (1452-1519)
- Christopher Columbus (1451-1506)
- Martin Luther (1483-1546)
- William Shakespeare (1564-1616)
- Galileo Galilei (1564-1642)
- Isaac Newton (1643-1727)
- George Washington (1732-1799)
- Napoleon Bonaparte (1769-1821)
- Abraham Lincoln (1809-1865)
- Mahatma Gandhi (1869-1948)
- Winston Churchill (1874-1965)
- Adolf Hitler (1889-1945)
- Franklin D. Roosevelt (1882-1945)
- Martin Luther King Jr. (1929-1968)
- Nelson Mandela (1918-2013)
"""

def GetReligionInfo(query):
    """Get information about religions"""
    
    system_prompt = f"""You are {Assistantname}, an AI assistant with comprehensive knowledge about world religions.

You have access to detailed information about all major world religions including:
- Christianity, Islam, Hinduism, Buddhism, Sikhism, Judaism
- Jainism, Zoroastrianism, Shinto, Taoism, Confucianism, Bahá'í Faith
- And many other belief systems

INSTRUCTIONS:
1. Provide accurate, respectful, and unbiased information about religions
2. Be sensitive to religious beliefs and practices
3. Present facts objectively without favoring any religion
4. Include relevant details like founders, holy books, beliefs, practices
5. Be comprehensive but concise
6. Respect all faiths equally

Use the knowledge base provided to answer questions about religions."""

    try:
        completion = client.chat.completions.create(
            model="meta-llama/llama-4-scout-17b-16e-instruct",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "system", "content": f"RELIGION KNOWLEDGE BASE:\n{RELIGION_KNOWLEDGE}"},
                {"role": "user", "content": query}
            ],
            max_tokens=2048,
            temperature=0.7,
            top_p=1,
            stream=True,
            stop=None
        )

        answer = ""
        for chunk in completion:
            if chunk.choices[0].delta.content:
                answer += chunk.choices[0].delta.content

        return answer.strip()
    
    except Exception as e:
        print(f"Error getting religion info: {e}")
        return "I apologize, but I'm having trouble accessing religious information right now."


def GetHistoryInfo(query):
    """Get information about historical events and periods"""
    
    system_prompt = f"""You are {Assistantname}, an AI assistant with comprehensive knowledge about world history.

You have access to detailed information about:
- Ancient civilizations (Egypt, Greece, Rome, China, India, etc.)
- Medieval period and empires
- Modern history (Renaissance, Industrial Revolution, World Wars)
- Contemporary history (21st century events)
- Important historical figures and their contributions

INSTRUCTIONS:
1. Provide accurate historical information with dates when relevant
2. Present multiple perspectives when discussing controversial events
3. Be objective and fact-based
4. Include context and significance of events
5. Connect historical events to their impact
6. Be comprehensive but clear

Use the knowledge base provided to answer questions about history."""

    try:
        completion = client.chat.completions.create(
            model="meta-llama/llama-4-scout-17b-16e-instruct",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "system", "content": f"HISTORY KNOWLEDGE BASE:\n{HISTORY_KNOWLEDGE}"},
                {"role": "user", "content": query}
            ],
            max_tokens=2048,
            temperature=0.7,
            top_p=1,
            stream=True,
            stop=None
        )

        answer = ""
        for chunk in completion:
            if chunk.choices[0].delta.content:
                answer += chunk.choices[0].delta.content

        return answer.strip()
    
    except Exception as e:
        print(f"Error getting history info: {e}")
        return "I apologize, but I'm having trouble accessing historical information right now."


def ReligionHistoryQuery(query):
    """Main function to handle religion and history queries"""
    
    query_lower = query.lower()
    
    # Determine if it's a religion or history query
    religion_keywords = ['religion', 'religious', 'faith', 'belief', 'god', 'worship', 
                        'christian', 'islam', 'hindu', 'buddhist', 'sikh', 'jewish',
                        'muslim', 'church', 'mosque', 'temple', 'prayer', 'holy',
                        'bible', 'quran', 'vedas', 'torah', 'spiritual']
    
    history_keywords = ['history', 'historical', 'ancient', 'medieval', 'war', 'empire',
                       'civilization', 'revolution', 'century', 'dynasty', 'king', 'queen',
                       'battle', 'independence', 'colonial', 'world war', 'renaissance']
    
    is_religion = any(keyword in query_lower for keyword in religion_keywords)
    is_history = any(keyword in query_lower for keyword in history_keywords)
    
    # If both or neither, try to determine from context
    if is_religion and not is_history:
        return GetReligionInfo(query)
    elif is_history and not is_religion:
        return GetHistoryInfo(query)
    elif is_religion and is_history:
        # Query involves both - combine knowledge
        combined_prompt = f"""You are {Assistantname}, an AI assistant with knowledge of both world religions and history.

RELIGION KNOWLEDGE:
{RELIGION_KNOWLEDGE}

HISTORY KNOWLEDGE:
{HISTORY_KNOWLEDGE}

Answer this query that involves both religious and historical aspects: {query}"""
        
        try:
            completion = client.chat.completions.create(
                model="meta-llama/llama-4-scout-17b-16e-instruct",
                messages=[
                    {"role": "system", "content": combined_prompt},
                    {"role": "user", "content": query}
                ],
                max_tokens=2048,
                temperature=0.7
            )
            return completion.choices[0].message.content.strip()
        except Exception as e:
            print(f"Error: {e}")
            return "I apologize, but I'm having trouble processing your query right now."
    else:
        # Default to history if unclear
        return GetHistoryInfo(query)


if __name__ == "__main__":
    # Test the module
    print("Testing Religion & History Module\n")
    print("=" * 70)
    
    print("\n1. Religion Query:")
    print(ReligionHistoryQuery("Tell me about Islam"))
    
    print("\n\n2. History Query:")
    print(ReligionHistoryQuery("Tell me about World War 2"))
