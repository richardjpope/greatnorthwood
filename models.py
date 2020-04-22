from helpers import get_config

class Tree:

  _photo = None

  @property
  def species_name(self):
    result = None
    config = get_config()
    keywords = self._photo.keywords
    for keyword in keywords:
      if keyword in config['species_tags']:
        result = keyword
        break
    return result

  @property
  def month_name(self):
    return self._photo.date.strftime("%B")

  @property
  def place_name(self):
    result = None
    if len(self._photo.place.names.area_of_interest) > 0:
      result = self._photo.place.names.area_of_interest[0]
    elif len(self._photo.place.names.additional_city_info) > 0:
      result = self._photo.place.names.additional_city_info[0]
    return result

  def __init__(self, photo):
    self._photo = photo