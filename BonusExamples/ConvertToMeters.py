from BonusExamples.ConverterMethods import convert_to_meters
from BonusExamples.ParsersMethods import parse

feet_inches = input("Enter feet and inches")

parsed = parse(feet_inches)
result = convert_to_meters(parsed['feet'], parsed['inches'])

print(f"{parsed['feet']} feet and {parsed['inches']} inches is equal to {result} meters")

if result < 1:
    print("Kid is too small")
else:
    print("Kid can use the slide.")
