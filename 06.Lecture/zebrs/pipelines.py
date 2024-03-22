from scrapy.pipelines.images import ImagesPipeline
import hashlib

class CustomImagesPipeline(ImagesPipeline):
    def file_path(self, request, response=None, info=None, *, item=None):
        item['name']
        # image_guid = hashlib.sha1(to_bytes(request.url)).hexdigest()
        image_guid = hashlib.sha1(request.url.encode()).hexdigest()
        folder_name = item['name'][0].replace(' ', '_').replace('|', 'I').replace('*', 'X').replace(',', '').replace('\'', '') \
        .replace('\"', '').replace('(', '').replace(')', '').replace('!', '').replace('?', '').replace(':', '') \
        .replace(';', '').replace('&', '').replace('/', '').replace('\\', '').replace('=', '').replace('+', 'plus')
        return f"{folder_name}/{image_guid}.jpg"
