import xml.etree.ElementTree as ET

class simplexmlparser:

    def __init__(self, xmlstring):

        self.domain = ET.fromstring(xmlstring)
        self.vmname = self.domain.find('name').text

        self.hostdev = self.domain.find('devices/hostdev')
        if self.hostdev:
            self.address = self.domain.find('devices/hostdev/source/address')
            self.metadev = self.domain.find("metadata/{http://ovirt.org/vm/1.0}vm/{http://ovirt.org/vm/1.0}device")
            mdevType = self.metadev.find('{http://ovirt.org/vm/1.0}mdevType').text.split('|')
            self.mdev_type = mdevType[0]
            self.mdev_placement = mdevType[1]
