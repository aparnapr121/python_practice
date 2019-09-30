import re

urls = '''
https://www.google.com
http://coreyms.com
https://youtube.com
https://www.nasa.gov
'''

pattern = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')
matches=pattern.finditer(urls)
subbed_urls = pattern.sub(r'\2\3',urls)
print(subbed_urls)
for match in matches:
    print(match.group(3))

matches=pattern.findall(urls)
print(matches)
for match in matches:
    print(match )

"""
pattern.finditer = Returns an iterator of all the match found in the text
pattern.findall = Returns a tuple of matched groups or the entire match if there are no groups
pattern.match = Returns a maatch found at the beginning of string
pattern.search = Returns first match at anywherein string
pattern.sub

"""

sentence = 'Test for 1234 match at beginning'
pattern = re.compile(r'\d+')
matches = re.match(pattern,sentence)
print(matches)
