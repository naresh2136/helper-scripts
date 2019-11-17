import os
import os.path
import re

import logging as log


def mkdir(dir, *dirs):
    # log.info("testing...")
    all_folders = [dir]
    all_folders.extend(dirs)
    for i in all_folders:
        if not isinstance(i, str):
            # log.error("Folder name '" + str(i) + "' is not a string")
            continue
        if not os.path.isdir(i):
            # log.info("Creating directory '" + i + "'")
            os.mkdir(i)
        else:
            print("Folder '" + str(i) + "' already exists")
        # log.warning("Folder '" + str(i) + "' already exists")


def get_username():
    user = os.popen("whoami")
    user = user.read().strip()
    log.info("Script executed by '" + user + "'")
    return user


def getcwd():
    cwd = os.getcwd()
    log.info("Working directory is '" + cwd + "'")
    return cwd


def get_ip_address():
    log.info("Finding IP address of system")
    fr_command = os.popen("ipconfig")
    out = fr_command.readlines()
    ips = []
    for i in out:
        i = i.strip()
        m = re.search("^\s*IPv4\s+Address.*:\s*(.+)", i)
        if m:
            ips.append(m.group(1))
            log.info("Found IP address '" + m.group(1) + "'")
    if len(ips) == 0:
        log.error("Could not find any ips")
    return ips


def get_all_folders(folder, ext=".*"):
    all_files = []
    for data in os.walk(folder):
        log.info("Traversing '" + data[0] + "'")
        for file in data[1]:
            m = re.search(ext, file)
            if not m:
                continue
            fpath = data[0] + "\\" + file
            all_files.append(fpath)
            log.debug("Found folder '" + fpath + "'")
    return all_files


def get_all_files(folder, ext=".*"):
    all_files = []
    log.info("Called 'get_all_files' to return all files from directory '" + folder + "'")
    for data in os.walk(folder):
        log.info("Traversing '" + data[0] + "'")
        for file in data[2]:
            m = re.search(ext, file)
            if not m:
                continue
            fpath = data[0] + "\\" + file
            all_files.append(fpath)
            log.debug("Found files '" + fpath + "'")
    return all_files


def is_empty_folder(folder):  # is_empty_folder({})
    if not isinstance(folder, str):
        log.error("Argument to 'is_empty_folder' expected to be a string")
        return None
    if not os.path.isdir(folder):
        log.error("Folder '" + folder + "' does not exists. Can not say empty or no")
        return None
    all_data = os.listdir(folder)
    if len(all_data) == 0:
        return True
    return False


def chdir(dir):
    if not os.path.isdir(dir):
        log.error("Could not change the directory. Invalid parameter to chdir, '" + dir + "' is not a directory")
        return
    log.info("Changing directory to '" + dir + "'")
    os.chdir(dir)


def basename(path):
    if not os.path.isfile(path):
        log.error("Invalid parameter to basename, '" + path + "' is not a file")
        return
    base = os.path.basename(path)
    log.info("Basename of file '" + path + "' is '" + base + "'")
    return base


def dirname(path):
    if not os.path.isfile(path):
        log.error("Invalid parameter to dirname, '" + path + "' is not a file")
        return
    dir = os.path.dirname(path)
    log.info("Dirname of file '" + path + "' is '" + dir + "'")
    return dir


def get_os_name():
    operating_system = sys.platform
    log.info("OS name is '" + operating_system + "'")
    return operating_system


def getsize(path):
    if not os.path.isfile(path):
        log.error("Invalid parameter to getsize, '" + path + "' is not a file")
        return
    size = os.path.getsize(path)
    log.info("Size of file '" + path + "' is" + str(size) + "'")
    return size


def getext(path):
    if not os.path.isfile(path):
        log.error("Invalid parameter to getext, '" + path + "' is not a file")
        return
    (dummy, ext) = os.path.splitext(path)
    log.info("Extension of file '" + path + "' is" + str(ext) + "'")
    return ext


def unlink(path):
    if not os.path.isfile(path):
        log.error("Invalid parameter to unlink, '" + path + "' is not a file")
        return
    os.unlink(path)
    log.info("Deleting file '" + path + "'")


def get_folder_size(folder, ext):
    log.info("Getting the size of folder '" + folder + "'")
    size = 0

    if not os.path.isdir(folder):
        log.error("Folder '" + folder + "' does not exist, can not find teh size of it")
        return size

    for data in os.walk(folder):
        log.info("Traeversing the folder '" + folder + "'")
        for file in data[2]:
            m = re.search(ext, file)
            if not m:
                continue
            fpath = data[0] + "\\" + file
            size = size + os.path.getsize(fpath)
    log.info("Folder '" + folder + "' size is " + str(size))
    return size


def read_excel(excel_file):
    wb = xlrd.open_workbook(excel_file)
    data = {}
    for sheet_name in wb.sheet_names():
        data[sheet_name] = []
        # print("Reading sheet", sheet_name)
        sheet1 = wb.sheet_by_name(sheet_name)
        nrows = sheet1.nrows
        ncols = sheet1.ncols

        sheet_data = []
        for i in range(nrows):
            row = []
            for j in range(ncols):
                # print(i, j, sheet1.cell_value(i, j))
                row.append(sheet1.cell_value(i, j))
            sheet_data.append(row)
        data[sheet_name] = sheet_data
    return data