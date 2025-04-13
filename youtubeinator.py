import os
if os.name == 'nt':
    yd = 'ytdlp.exe'
    fm = 'ffmpeg.exe'
    if os.path.isfile(yd):
        pass
    else:
        raise ModuleNotFoundError("./ytdlp.exe does not exist. download it at https://github.com/yt-dlp/yt-dlp/releases/latest")
    if os.path.isfile(fm):
        pass
    else:
        raise ModuleNotFoundError("./ffmpeg.exe does not exist. download it at https://www.ffmpeg.org/download.html")
elif os.name == 'posix':
    yd = 'ytdlp'
    fm = 'ffmpeg'
    if os.path.isfile(yd):
        pass
    else:
        raise ModuleNotFoundError("./ytdlp does not exist. download it at https://github.com/yt-dlp/yt-dlp/releases/latest")
    if os.path.isfile(fm):
        pass
    else:
        raise ModuleNotFoundError("./ffmpeg does not exist. download it at https://www.ffmpeg.org/download.html")

class VideoDownloadParameters:
    def __init__(self, fps="30", resolution="1920:1080", outformat="avi", audiobitrate="128k", videobitrate="1000k", sponsorblock=False, sponsorblock_cats="all", sponsorblock_api="https://sponsor.ajay.app"):
        self.fps = fps
        self.resolution = resolution
        self.outformat = outformat
        self.abitrate = audiobitrate
        self.vbitrate = videobitrate
        self.sb = sponsorblock
        self.sb_categories = sponsorblock_cats
        self.sb_api = sponsorblock_api
    def shellcommand_tres(self):
        if os.name == 'nt':
            return f"del out.tmp"
        elif os.name == 'posix':
            return f"rm out.tmp"
        else:
            print("Unknown OS, you gotta delete the file yourself :/")
    def shellcommand_dos(self,outf):
        return f"{fm} -i out.tmp -vf \"scale={self.resolution}\" {outf}"
    def shellcommand_uno(self,ytid):
        return f"{yd} --verbose --windows-filenames "+("--no-sponsorblock" if not self.sb else "")+f" --recode-video {self.outformat} --sponsorblock-remove {self.sb_categories} --sponsorblock-api {self.sb_api} --postprocessor-args ffmpeg:\"-r {self.fps} -b:a {self.abitrate} -b:v {self.vbitrate}\" -o \"out.tmp\" \"https://youtube.com/watch?v={ytid}\""

class VideoDownload:
    def __init__(self, ytid, outf, paramobject):
        if not (isinstance(paramobject, VideoDownloadParameters)):
            raise ValueError('the video download parameters are not an instance of VideoDownloadParameters')
        self.ytid = ytid
        self.param = paramobject
        self.outf = outf
    def start(self):
        os.system(self.param.shellcommand_uno(self.ytid))
        os.system(self.param.shellcommand_dos(self.outf))
        os.system(self.param.shellcommand_tres())