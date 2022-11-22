import click
from termcolor import colored, cprint
import pyfiglet
import os

@click.command()
@click.option('--cv','cv',is_flag=True,help="download my CV")
@click.option('--LI','linkedin',is_flag=True,help="Show my LinkedIn profile")
@click.option('--gh','github',is_flag=True,help="Show my github")
@click.option('--about','about',is_flag=True,help="i will let you know about me a little bit 😍")
def init(cv,linkedin,about,github):
    '''
    This is a simple CLI to show my CV and resume
    '''
    result = pyfiglet.figlet_format("Amir M. Ghanem")
    _cvdownloadtext = colored(pyfiglet.figlet_format("CV Downloader!"),"cyan")
    text = colored(result, "cyan")
    print(text)
    print(_cvdownloadtext)
    if cv:
        # download location path
        desktop = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop')
        file_name="cv.pdf"
        completepath = desktop + "/" + file_name
        file_path = os.path.join(os.path.dirname(__file__), 'Assets/Amir_Ghanem_CV.pdf')
        cv = open(file_path, 'rb')
        file=open(completepath, 'wb')
        file.write(cv.read())
        print("CV Downloaded!")
    if linkedin:
        print("Visit my LinkedIn profile:https://www.linkedin.com/in/amir-ghanem-1b5a021b5/")
    if about:
        print("I AM AMIR :) I AM 27 YEARS OLD AND I AM A SOFTWARE ENGINEER AND I AM A PYTHON DEVELOPER")
    if github:
        print("Visit my GitHub profile: https://www.github.com/AmirMGhanem")





