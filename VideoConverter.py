import os

class VideoConverter():
  __ENCODER  = None
  __FPS = None
  __SIZE = None
  __EXTENSION = None
  __DEVICES = {'iphone': '161x283', 'macbook': '400x300', 'imac': '1000x800'}

  def __init__(self,
               encoder="ffmpeg",
               fps=30):

    self.set_encoder(encoder)
    self.set_fps(fps)

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
      #TODO: Add other formats, if required.
      pass

  def output_format(self, format):
    for devices in self.get_devices():
      if devices == format:
        self.set_size(self.get_device_size(format))
      else:
        #TODO: Handle error or return a default size.
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

  def get_devices(self):
    """
    :return dict:
    """
    return VideoConverter.__DEVICES

  def get_device_size(self, device):
    """
    :param device:
    :return mixed:
    """
    return VideoConverter.__DEVICES[device]