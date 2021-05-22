import docker
from tkinter import filedialog
import os
import tarfile
from colors import bcolors


def open_file():
    path = filedialog.askopenfilename()
    return path


def open_dir():
    path = filedialog.askdirectory()
    return path


def copy_to(src, dst):
    name, dst = dst.split(':')
    container = client.containers.get(name)

    os.chdir(os.path.dirname(src))
    srcname = os.path.basename(src)
    tar = tarfile.open(src + '.tar', mode='w')
    try:
        tar.add(srcname)
    finally:
        tar.close()

    data = open(src + '.tar', 'rb').read()
    container.put_archive(os.path.dirname(dst), data)


def copy_from(src, dst):
    name, path = src.split(":")
    container = client.containers.get(name)
    strm, stat = container.get_archive(path)
    with open(f"{dst}.tar", 'wb') as outfile:
        for d in strm:
            outfile.write(d)
    os.chdir("/".join(dst.split("/")[:-1]))
    tarfile.open(f"{dst}.tar").extractall()
    os.remove(f"{dst}.tar")


if __name__ == '__main__':
    client = docker.from_env()
    print(
        bcolors.OKCYAN
        + """
         __      __    _       _____       _            _   
         \ \    / /   | |     |  __ \     | |          | |  
          \ \  / /   _| |_ __ | |  | | ___| |_ ___  ___| |_ 
           \ \/ / | | | | '_ \| |  | |/ _ \ __/ _ \/ __| __|
            \  /| |_| | | | | | |__| |  __/ ||  __/ (__| |_ 
             \/  \__,_|_|_| |_|_____/ \___|\__\___|\___|\__|


            """
        + bcolors.ENDC
    )
    print(
        bcolors.BOLD
        + bcolors.OKGREEN
        + "Welcome to VulnDetect."
        + bcolors.ENDC
        + bcolors.ENDC
    )
    print(bcolors.OKGREEN + "Make a choice:" + bcolors.ENDC)
    print(
        bcolors.WARNING + "1. Choose a file with a website list." + bcolors.ENDC
    )
    print(
        bcolors.WARNING + "2. Scrape a given website or domain." + bcolors.ENDC
    )
    print(bcolors.WARNING + "3. Write down a website to check" + bcolors.ENDC)
    print(bcolors.FAIL + "0. EXIT()" + bcolors.ENDC)
    choice = input("Your choice: ")
    name = "vulndetect"
    os.system("docker pull cioboteavlad1/vulndetect")
    os.system(f'docker run -it -d --name {name} -e "CHOICE={choice}" -e "TERM=xterm" cioboteavlad1/vulndetect')
    os.system("clear")
    if choice == "1":
        file = open_file()
        copy_to(
            file,
            f"{name}:/tmp/site.txt"
        )
    print("Now choose a folder to save the reports in.")
    dir = open_dir()
    print("Press enter to continue.")
    os.system(f"docker attach {name}")
    try:
        copy_from(f"{name}:/tmp/found_get_sqlis.txt",
                  f"{dir}/found_get_sqlis.txt")
        copy_from(f"{name}:/tmp/found_post_sqlis.txt",
                  f"{dir}/found_post_sqlis.txt")
        copy_from(f"{name}:/tmp/found_lfis.txt",
                  f"{dir}/found_lfis.txt")
        copy_from(f"{name}:/tmp/found_rfis.txt",
                  f"{dir}/found_rfis.txt")
    except Exception:
        os.system(f"docker rm {name}")
