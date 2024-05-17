"""Módulo principal"""

import os

# import shutil
import sys
import subprocess


def check_disks(directory):
    """Check path exits"""

    if not os.path.exists(directory):
        print(f"• Directorio no encontrado: {directory}")
        sys.exit()
        
def check_destination_disk(destination_dir):
    """Create the subfolder if doesn't exist"""
    # subfolder_path = os.path.join(destination_dir, )
    pass
    # TODO


def main(source_dir, destination_dir, is_testing, is_verbose, create_backup):
    """Funcion principal"""

    check_disks(source_dir)
    #check_disks(destination_dir)
    #  •

    # To avoid data loss by accidentally swapping the SOURCE and DESTINATION arguments
    dont_make_changes = "-n"
    # '-n' as default

    # to reduce logging verbosity. -q as default
    verbose = "-q"

    # Default
    cmd = ["rsync-system-backup"]
    cmd.append(source_dir)
    cmd.append(destination_dir)

    cmd.append(dont_make_changes)
    cmd.append(verbose)

    msg = ["Default", cmd]

    print(f"Pass 1: {msg[0]}: {msg[1]}")

    if create_backup:
        # start backup
        cmd.remove("-n")
        cmd.append("-b")
        msg[0] = 'Backup'
        print(f"Pass 2: {msg[0]}: {msg[1]}")

        if is_verbose:
            cmd.remove("-q")
            cmd.append("-v")
            msg[0] = "Backup w/ more verbosity"
        else:
            # cmd.append('-q')
            msg[0] = "Backup w/ less verbosity"

        print(f"Pass 3: {msg[0]}: {msg[1]}")
    else:
        # testing mode
        msg[0] = "Test the backup"

        if is_testing and is_verbose:
            cmd.remove("-q")
            cmd.append("-v")
            print(f"Pass 4: {msg[0]}: {msg[1]}")


    try:
        # do_start_backup = subprocess.run(
        #     ["rsync-system-backup", sdir, ddir, arg1, arg2], check=False, shell=False)
        do_start_backup = subprocess.run(cmd, check=False, shell=False)
        # do_start_backup = subprocess.run([cmd], check=False, shell=False)
        # do_start_backup = subprocess.run(["rsync"], shell=False, check=False)
    except subprocess.CalledProcessError as err:
        print("Comando falló con el error: ", err.returncode)
    else:
        print("returncode: ", do_start_backup.returncode)
        print(f"stdout is {do_start_backup.stdout}")
        print(f"stderr is {do_start_backup.stderr}")

    # print(dont_make_changes, verbose, start_backup)

    # print(cmd)
