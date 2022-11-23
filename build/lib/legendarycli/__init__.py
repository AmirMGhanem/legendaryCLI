import click
import requests
from termcolor import colored, cprint
import pyfiglet
import os
from tqdm import tqdm

@click.command()
@click.option('--cv','cv',is_flag=True,help="download my CV , Please Specify which OS you")
@click.option('--mac','mac',is_flag=True,help="download cv for macOS users - path: /Desktop")
@click.option('--win','win',is_flag=True,help="download cv for windows users  - path: /Desktop")
@click.option('--li','linkedin',is_flag=True,help="Show my LinkedIn profile")
@click.option('--gh','github',is_flag=True,help="Show my github")
@click.option('--about','about',is_flag=True,help="i will let you know about me a little bit 😍")
def init(cv,linkedin,about,github,mac,win):
    '''
    This is a simple CLI to show my CV and resume
    '''
    result = pyfiglet.figlet_format("Amir M. Ghanem")
    _cvdownloadtext = colored(pyfiglet.figlet_format("CV Downloader!"), "cyan")
    text = colored(result, "cyan")
    print(text)

    if cv:
        print(_cvdownloadtext)
        # download location path
        if mac:
            desktop = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop')
        elif win:
            desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
        else:
            _error = colored(pyfiglet.figlet_format("Specify Your OS"), "red")
            print(_error)
            return 0
        file_name="cv.pdf"
        completepath = desktop + "/" + file_name
        file_url = "https://p-lux4.pcloud.com/D4Zkn0yP1Z1hr6bPZZZjDo9c7Z2ZZjFRZkZWyFXZlzZnHZjzZAeptXZtxgqMPTvCJmEp38X89Wi47iFtgxy/Amir%20Ghanem%20CV.pdf"
        cv = requests.get(file_url, 'rb')
        file=open(completepath, 'wb')
        file.write(cv.content)
        for i in tqdm(range(int(9e6))):
            pass
        print("CV Downloaded!")
    if linkedin:
        print("Visit my LinkedIn profile:https://www.linkedin.com/in/amir-ghanem-1b5a021b5/")
    if about:
        print("I AM AMIR :) I AM 27 YEARS OLD AND I AM A SOFTWARE ENGINEER AND I AM A PYTHON DEVELOPER")
    if github:
        print("Visit my GitHub profile: https://www.github.com/AmirMGhanem")




if __name__ == '__main__':
    init()
