from moviepy.editor import VideoFileClip


def mp4_to_gif(path_for_tiktok, path_output_video):
    video = VideoFileClip(path_for_tiktok)
    video.write_gif(path_output_video)


input = "https://v16-webapp.tiktok.com/8e2a9dc112af7d29813c58babfa61ca8/62e822b6/video/tos/useast2a/tos-useast2a-ve-0068c003/10dc97771396494f9fb8ee304afa1909/?a=1988&ch=0&cr=0&dr=0&lr=tiktok_m&cd=0%7C0%7C1%7C0&cv=1&br=2516&bt=1258&btag=80000&cs=0&ds=3&ft=eXd.6H-oMyq8Zy~F1we2NEv4yl7Gb&mime_type=video_mp4&qs=0&rc=ODw4OjQ7ZjY1OmY8Njw4ZEBpMzc3NTk6ZjlzZDMzNzczM0A0M18tYy1gNl4xNi5fNmM2YSNiXmowcjQwZWxgLS1kMTZzcw%3D%3D&l=20220801125923010217029141062BC982"
output = "test.gif"
mp4_to_gif(input, output)
