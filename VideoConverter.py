import os

class VideoConverter():
  __ENCODER  = None
  __FPS = None
  __SIZE = None
  __EXTENSION = None

  def __init__(self,
               encoder="ffmpeg",
               fps=20,
               size="600x338"):

    self.set_encoder(encoder)
    self.set_fps(fps)
    self.set_size(size)

  def input_file_name(self, video):
    """
    :param video:
    """
    self.video = video

  def output_file_name(self, name):
    """
    :param name:
    """
    name = name.split('.')
    self.output_name = name[0]

    if name[1] == 'gif':
      self.set_extension('gif')
    else:
      pass

  def generate_gif(self):
    os.system(
      "%s -i %s -r %s -s %s %s.%s"
      %(self.get_encoder(),
        self.video,
        self.get_fps(),
        self.get_size(),
        self.output_name,
        self.get_extension()
        )
    )

  def set_extension(self, extension):
    """
    :param extension:
    """
    VideoConverter.__EXTENSION = extension

  def set_size(self, size):
    """
    :param size:
    """
    VideoConverter.__SIZE = size

  def set_fps(self, fps):
    """
    :param fps:
    """
    VideoConverter.__FPS = fps

  def set_encoder(self, encoder):
    """
    :param encoder:
    """
    VideoConverter.__ENCODER = encoder

  def get_extension(self):
    """
    :return mixed:
    """
    return VideoConverter.__EXTENSION

  def get_size(self):
    """
    :return mixed:
    """
    return VideoConverter.__SIZE

  def get_fps(self):
    """
    :return mixed:
    """
    return VideoConverter.__FPS

  def get_encoder(self):
    """
    :return mixed:
    """
    return VideoConverter.__ENCODER