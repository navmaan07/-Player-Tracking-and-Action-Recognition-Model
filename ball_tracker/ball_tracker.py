import numpy as np
import cv2

class BallTracker:
    def __init__(self):
        self.ball_route = []

    def trace_ball_route(self, tracks):
        for frame_num, ball_track in enumerate(tracks['ball']):
            if ball_track:
                ball_id, ball_info = list(ball_track.items())[0]
                if 'transformed_position' in ball_info:
                    x, y = ball_info['transformed_position']
                    self.ball_route.append((frame_num, x, y))

    def draw_ball_route(self, video_frames):
        route = np.array(self.ball_route)
        
        for frame_num, frame in enumerate(video_frames):
            # Draw the entire route up to the current frame
            current_route = route[route[:, 0] <= frame_num]
            
            if len(current_route) > 1:
                for i in range(1, len(current_route)):
                    start = tuple(map(int, current_route[i-1, 1:]))
                    end = tuple(map(int, current_route[i, 1:]))
                    cv2.line(frame, start, end, (0, 255, 255), 2)  # Yellow line
            
            # Draw the current ball position
            if len(current_route) > 0:
                current_pos = tuple(map(int, current_route[-1, 1:]))
                cv2.circle(frame, current_pos, 5, (0, 0, 255), -1)  # Red circle
        
        return video_frames