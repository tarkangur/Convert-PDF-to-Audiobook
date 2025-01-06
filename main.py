import boto3
from pypdf import PdfReader


reader = PdfReader("example0.pdf")
text = reader.pages[0].extract_text()


polly = boto3.Session(
    aws_access_key_id=" ",
    aws_secret_access_key=" ",
    region_name="us-west-2").client("polly")

response = polly.synthesize_speech(VoiceId="Joanna",
                                   OutputFormat="mp3",
                                   Text=text,
                                   Engine="neural")
file = open("speech.mp3", "wb")
file.write(response["AudioStream"].read())
file.close()
