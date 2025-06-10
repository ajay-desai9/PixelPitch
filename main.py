from utils import read_video, save_video
from tracking.tracker import Tracker

def main():
    
    video_frames = read_video("input_videos/08fd33_4.mp4")

    tracker = Tracker("models/best.pt")

    tracks = tracker.get_object_tracks(video_frames,
                                       read_from_stub=True,
                                       stub_path="stubs/track_stubs.pkl")
    
    tracker.add_position_to_tracks(tracks)

    
    ## Draw object Tracks
    output_video_frames = tracker.draw_annotations(video_frames, tracks,team_ball_control)

    save_video(output_video_frames, "output_videos/output_video.mp4")


if __name__ == '__main__':
    main()
