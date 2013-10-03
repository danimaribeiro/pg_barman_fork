#coding=utf-8
from abc import ABCMeta, abstractmethod
from boto.s3.connection import S3Connection
from boto.s3.key import Key


class StorageAbstract(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def Save(self, backup, config):
        pass
      
      
class AmazonS3(StorageAbstract):        
    
    def Save(self, backup, config):  
        conn = S3Connection(config['access_key'], config['secret_key'])
        bucket = conn.create_bucket('get_name_from_backup')
        
        newKey = Key(bucket)
        newKey.name = backup.description
        newKey.key = backup.name
        newKey.set_contents_to_filename(backup.file_location)    

class FtpStorage(StorageAbstract):
  
    def Save(self, backup, config):
        pass
      
class AzureBlob(StorageAbstract):
    def Save(self, backup, config):
      pass

      
      
      