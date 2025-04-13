import youtubeinator as yi
vdp = yi.VideoDownloadParameters(outformat="mp4", resolution="640:480")
vd = yi.VideoDownload(input('video id>'),"out.mp4",vdp)
vd.start()