import asyncio
from shazamio import Shazam, Serialize


async def main():
  shazam = Shazam()
  top_tracks = await shazam.top_city_tracks(country_code='US', city_name='Philadelphia', limit=10)
  # ALL TRACKS DICT
  for track in top_tracks['tracks']:
      serialized = Serialize.track(data=track)
      # SERIALIZE FROM DATACLASS FACTORY
      print(serialized)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
