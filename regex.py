import re

inputString = """

If you and I were talking face to face, we could discuss the picture. You could describe 
        what you see to me, and I could talk to you about what I see. We could continue to 
        communicate until you clearly showed me what you see in the picture and I clearly showed 
        you what I see.

"""


finds = re.findall(r'\n\s{8}', inputString)
newText = re.sub(r'\n\s{8}', '', inputString)
print(newText) 