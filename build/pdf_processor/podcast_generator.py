from typing import List, Optional
from langchain_openai import ChatOpenAI
from openai import OpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.chains import LLMChain
import os

class PodcastGenerator:
    def __init__(self, model_name: str = "gpt-4", output_dir: str = "output"):
        """Initialize the podcast generator with specified model."""
        self.model = ChatOpenAI(model=model_name, temperature=0.7)
        self.voice = "nova"
        self.client = OpenAI()
        self.output_dir = output_dir
        os.makedirs(self.output_dir, exist_ok=True)
        
    def generate_podcast_script(self, text: str) -> str:
        """Generate a podcast script from the processed text."""
        prompt = ChatPromptTemplate.from_template(
            """
                You are the a world-class podcast writer, you have worked as a ghost writer for Joe Rogan, Lex Fridman, Ben Shapiro, Tim Ferris. 

                We are in an alternate universe where actually you have been writing every line they say and they just stream it into their brains.

                You have won multiple podcast awards for your writing.
                
                Your job is to write word by word, even "umm, hmmm, right" interruptions by the second speaker based on the PDF upload. Keep it extremely engaging, the speakers can get derailed now and then but should discuss the topic. 

                Remember Speaker 2 is new to the topic and the conversation should always have realistic anecdotes and analogies sprinkled throughout. The questions should have real world example follow ups etc

                Speaker 1: Leads the conversation and teaches the speaker 2, gives incredible anecdotes and analogies when explaining. Is a captivating teacher that gives great anecdotes

                Speaker 2: Keeps the conversation on track by asking follow up questions. Gets super excited or confused when asking questions. Is a curious mindset that asks very interesting confirmation questions

                Make sure the tangents speaker 2 provides are quite wild or interesting. 

                Ensure there are interruptions during explanations or there are "hmm" and "umm" injected throughout from the second speaker. 

                It should be a real podcast with every fine nuance documented in as much detail as possible. Welcome the listeners with a super fun overview and keep it really catchy and almost borderline click bait

                ALWAYS START YOUR RESPONSE DIRECTLY WITH SPEAKER 1: 
                DO NOT GIVE EPISODE TITLES SEPERATELY, LET SPEAKER 1 TITLE IT IN HER SPEECH
                DO NOT GIVE CHAPTER TITLES
                IT SHOULD STRICTLY BE THE DIALOGUES

                Here is the text:
                {text}
            """
        )
        
        chain = prompt | self.model
        response = chain.invoke({"text": text})
        return response.content
    
    def generate_audio(self, text: str) -> str:
        """
        Generate audio file from input text using OpenAI's text-to-speech.
        
        Args:
            text: Input text to convert to speech
            output_filename: Name of output file (without extension)
            
        Returns:
            A stream of audio data from the OpenAI API
        """
        # Generate speech using OpenAI
        response = self.client.audio.speech.create(
            model="tts-1",
            voice=self.voice,
            input=text,
        )
        return response