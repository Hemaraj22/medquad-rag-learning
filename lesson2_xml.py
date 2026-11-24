import xml.etree.ElementTree as ET
from pathlib import Path

files = sorted(Path("MedQuAD/5_NIDDK_QA").glob("*.xml"))
print(len(files), "files in this folder")

root = ET.parse(files[0]).getroot()
print("source:", root.attrib.get("source"))
print("url:", root.attrib.get("url"))
print("focus:", root.findtext("Focus"))

for pair in root.find("QAPairs").findall("QAPair"):
    print("\nQ:", pair.findtext("Question"))
    print("A:", (pair.findtext("Answer") or "")[:150], "...")

    