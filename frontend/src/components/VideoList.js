import React from 'react';

function VideoList({ videos }) {
  return (
    <div className="results-section">
      <h2>Related Videos</h2>
      {videos.length > 0 ? (
        <ul className="results-list video-list">
          {videos.map((video, index) => (
            <li key={index} className="result-item video-item">
              <a href={video.url} target="_blank" rel="noopener noreferrer">
                {video.title}
              </a>
              <p>{video.description.substring(0, 120)}...</p>
            </li>
          ))}
        </ul>
      ) : (
        <p>No videos found.</p>
      )}
    </div>
  );
}

export default VideoList;