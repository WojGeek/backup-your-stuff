"""Módulo principal : Backup your stuff

"""

import os
import sys
import subprocess

from helpers.exclude import Exclude


def check_disks(directory):
    """Check path exits"""

    if not os.path.exists(directory):
        print(f"• Directorio no encontrado: {directory}")
        sys.exit()


def suggest_destination(source):
    """
    Create the subfolder from source directory

    """
    dest_dir = os.path.basename(os.path.normpath(source))

    return dest_dir


def make_separate_list_exclusions(_command):
    """make a list of excludes"""

    exclude_list = Exclude("exclude.json").load_items()

    # args["patterns"] = EXCLUDE
    command_plus_args = _command
    for directory in exclude_list:
        # print(directory)
        command_plus_args.append("--exclude")
        command_plus_args.append(directory)

    return command_plus_args


def main(args):
    # def main(source_dir, destination_dir, is_testing, is_verbose, create_backup, excludes=False):
    """Main - Sync / Files Backup

    Parameter:

        args (dict):

            args.origen: source directory
            .
            .
            args.patterns:  list of excludes

    """

    (source_dir, destination_dir, is_testing, is_verbose, is_backup, excluding) = (
        args.values()
    )

    # Directories
    check_disks(source_dir)

    # Create destination
    destination_dir = os.path.join(destination_dir, suggest_destination(source_dir))

    # To avoid data loss by accidentally swapping the SOURCE and DESTINATION arguments
    dont_make_changes = "--dry-run"
    # '-n' as default

    # to reduce logging verbosity. -q as default
    verbose = "--quiet"

    # Default
    cmd = ["rsync-system-backup"]

    cmd.append(source_dir)
    cmd.append(destination_dir)

    cmd.append(dont_make_changes)
    cmd.append(verbose)

    msg = ["Default", cmd]

    print(f"CMD Set 1: {msg[0]}: {msg[1]}")

    if is_backup:
        # start backup
        cmd.remove("--dry-run")
        cmd.append("--backup")
        msg[0] = "Backup"
        print(f"CMD Set 2: {msg[0]}: {msg[1]}")

        if is_verbose:
            cmd.remove("--quiet")
            cmd.append("--verbose")
            msg[0] = "Backup w/ more verbosity"
        else:
            # cmd.append('-q')
            msg[0] = "Backup w/ less verbosity"

        print(f"Cmd set 3: {msg[0]}: {msg[1]}")
    else:
        # testing mode
        msg[0] = "Test the backup"

        if is_testing and is_verbose:
            cmd.remove("--quiet")
            cmd.append("--verbose")
            print(f"CMD Set 4: {msg[0]}: {msg[1]}")

    # --exclude=EXCLUDE_PATTERN
    if excluding:
        cmd = make_separate_list_exclusions(cmd)

    # Let the party begin   ;)
    try:

        if is_verbose:
            do_start_backup = subprocess.run(cmd, check=False, shell=False)
        else:
            do_start_backup = subprocess.run(
                cmd, check=False, shell=False, stdout=subprocess.DEVNULL
            )

    except subprocess.CalledProcessError as err:
        print("Comando falló con el error: ", err.returncode)
    else:
        print("returncode: ", do_start_backup.returncode)
        # print(f"stdout is {do_start_backup.stdout}")
        print(f"stderr is {do_start_backup.stderr}")

    status = (
        "Ejecutado con éxito" if do_start_backup.returncode == 0 else "- Hubo fallos"
    )
    print(status)
    print("---")
    if excluding:
        print(
            "- Exclude files matching PATTERN Applied.\n\t More info, check: python exclude.py "
        )

    if not is_testing:
        print("- Check backup at: ", destination_dir)
