# -*- coding: utf-8 -*-
# !/usr/bin/python3

import os


def readCrontab():
    # Generate crontab file
    crontabFile = "/home/pi/crontab.txt"
    os.system("crontab -l > " + crontabFile)

    # Open crontab file
    with open(crontabFile) as inFile:
        cronjobs = [job.replace("\n", "") for job in inFile.readlines()]
    os.remove(crontabFile)

    # Parse jobs and their status
    cronjobs = [{"job": job, "status": "disabled" if job.startswith("#") else "enabled"} for job in cronjobs]

    return cronjobs


def saveCrontab(cronjobs):
    try:
        newCrontab = []
        for job in cronjobs:
            jobJob = job["job"]
            jobStatus = job["status"]
            jobJob = jobJob[1:] if jobJob.startswith("#") else jobJob if jobStatus == "enabled" else "#" + jobJob if not jobJob.startswith("#") else jobJob
            newCrontab.append(jobJob + "\n")

        crontabFile = "/home/pi/crontab.txt"
        with open(crontabFile, "w") as outFile:
            outFile.writelines(newCrontab)

        os.system("crontab -u pi " + crontabFile)
        os.remove(crontabFile)
        return "success", "Crontab saved successfully!"
    except Exception as ex:
        return "error", str(ex)
