from abc import ABCMeta, abstractmethod

class StorageAbstract(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def Save(self, backup, config):
        pass
      
      
class AmazonS3(StorageAbstract):
    pass
  
  
AmazonS3()
      
      
      