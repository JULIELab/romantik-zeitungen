import os
import datetime

lccn = "BV002720696"

volume_list = input("Volume list:")
with open(volume_list,"r",encoding="utf-8") as f:
	volumes = f.readlines()

issue = 0
with open("../../batch.xml","w",encoding="utf-8") as f:
	f.write('<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n')
	f.write('<ndnp:batch xmlns:ndnp=\"http://www.loc.gov/ndnp\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xmlns=\"http://www.loc.gov/ndnp\" name=\"batch_demnbsb_amz\" awardee=\"demnbsb\" awardYear=\"2009\">\n')
with open("../../batch_1.xml","w",encoding="utf-8") as f:
	f.write('<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n')
	f.write('<ndnp:batch xmlns:ndnp=\"http://www.loc.gov/ndnp\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xmlns=\"http://www.loc.gov/ndnp\" name=\"batch_demnbsb_amz\" awardee=\"demnbsb\" awardYear=\"2009\">\n')

for volume in volumes:
	time = str(datetime.datetime.now().replace(microsecond=0).isoformat())
	volume_num = str(int(volume[0:4])-1797)
	issue += 1
	folder = volume.strip()
	print(folder)

	with open("../../batch.xml","a",encoding="utf-8") as f:
		f.write('\t<issue lccn=\"')
		f.write(lccn)
		f.write('\" issueDate=\"')
		f.write(volume[0:4])
		f.write('-')
		f.write(volume[4:6])
		f.write('-')
		f.write(volume[6:8])
		f.write('\" editionOrder=\"01\">')
		f.write(lccn)
		f.write('/print/')
		f.write(folder)
		f.write('/')
		f.write(folder)
		f.write('.xml</issue>\n')
	with open("../../batch_1.xml","a",encoding="utf-8") as f:
		f.write('\t<ndnp:issue lccn=\"')
		f.write(lccn)
		f.write('\" issueDate=\"')
		f.write(volume[0:4])
		f.write('-')
		f.write(volume[4:6])
		f.write('-')
		f.write(volume[6:8])
		f.write('\" editionOrder=\"01\">')
		f.write(lccn)
		f.write('/print/')
		f.write(folder)
		f.write('/')
		f.write(folder)
		f.write('.xml</ndnp:issue>\n')

	os.chdir(folder)
	with open(folder+".xml","w",encoding="utf-8") as f:
		f.write('<?xml version=\"1.0\" encoding=\"UTF-8\"?>')
		f.write('\n')
		f.write('<mets TYPE=\"urn:library-of-congress:ndnp:mets:newspaper:issue\" PROFILE=\"urn:library-of-congress:mets:profiles:ndnp:issue:v1.5\" LABEL=\"Allgemeine Musikalische Zeitung,')
		f.write(volume[0:4])
		f.write('-')
		f.write(volume[4:6])
		f.write('-')
		f.write(volume[6:8])
		f.write('\"\n')
		f.write('\txmlns:mix=\"http://www.loc.gov/mix/\" xmlns:ndnp=\"http://www.loc.gov/ndnp\" xmlns:premis=\"http://www.oclc.org/premis\" xmlns:mods=\"http://www.loc.gov/mods/v3\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xmlns:xlink=\"http://www.w3.org/1999/xlink\" xmlns=\"http://www.loc.gov/METS/\"\n')
		f.write('\txsi:schemaLocation=\"\n')
		f.write('\thttp://www.loc.gov/METS/ http://www.loc.gov/standards/mets/version17/mets.v1-7.xsd\n')
		f.write('\thttp://www.loc.gov/mods/v3 http://www.loc.gov/standards/mods/v3/mods-3-3.xsd\">\n')
		f.write('\t<!--METS HEADER-->\n')
		f.write('\t<metsHdr CREATEDATE=\"')
		f.write(time)
		f.write('\">\n')
		f.write('\t\t<agent ROLE=\"CREATOR\" TYPE=\"ORGANIZATION\">\n')
		f.write('\t\t\t<name>JULIE Lab</name>\n')
		f.write('\t\t</agent>\n')
		f.write('\t</metsHdr>\n')
		f.write('\t<!--DESCRIPTIVE METADATA-->\n')
		f.write('\t<dmdSec ID=\"issueModsBib\">\n')
		f.write('\t\t<mdWrap MDTYPE=\"MODS\" LABEL=\"Issue metadata\">\n')
		f.write('\t\t\t<xmlData>\n')
		f.write('\t\t\t\t<mods:mods>\n')
		f.write('\t\t\t\t\t<mods:relatedItem type=\"host\">\n')
		f.write('\t\t\t\t\t\t<mods:identifier type=\"lccn\">')
		f.write(lccn)
		f.write('</mods:identifier>\n')
		f.write('\t\t\t\t\t\t<mods:part>\n')
		f.write('\t\t\t\t\t\t\t<mods:detail type=\"volume\">\n')
		f.write('\t\t\t\t\t\t\t\t<mods:number>')
		f.write(volume_num)
		f.write('</mods:number>\n')
		f.write('\t\t\t\t\t\t\t</mods:detail>\n')
		f.write('\t\t\t\t\t\t\t<mods:detail type=\"issue\">\n')
		f.write('\t\t\t\t\t\t\t\t<mods:number>')
		f.write(str(issue))
		f.write('</mods:number>\n')
		f.write('\t\t\t\t\t\t\t</mods:detail>\n')
		f.write('\t\t\t\t\t\t\t<mods:detail type=\"edition\">\n')
		f.write('\t\t\t\t\t\t\t\t<mods:number>')
		f.write('1')
		f.write('</mods:number>\n')
		f.write('\t\t\t\t\t\t\t</mods:detail>\n')
		f.write('\t\t\t\t\t\t</mods:part>\n')
		f.write('\t\t\t\t\t</mods:relatedItem>\n')
		f.write('\t\t\t\t\t<mods:originInfo>\n')
		f.write('\t\t\t\t\t\t<mods:dateIssued encoding=\"iso8601\">')
		f.write(volume[0:4])
		f.write('-')
		f.write(volume[4:6])
		f.write('-')
		f.write(volume[6:8])
		f.write('</mods:dateIssued>\n')
		f.write('\t\t\t\t\t</mods:originInfo>\n')
		f.write('\t\t\t\t\t<mods:note type=\"noteAboutReproduction\">Present</mods:note>\n')
		f.write('\t\t\t\t</mods:mods>\n')
		f.write('\t\t\t</xmlData>\n')
		f.write('\t\t</mdWrap>\n')
		f.write('\t</dmdSec>\n')
		num = 0
		for page in os.listdir():
			if page.endswith('pdf'):
				if int(page.split('.pdf')[0]) > num:
					num = int(page.split('.pdf')[0])
		for i in range(1,num+1):
			f.write('\t<dmdSec ID=\"pageModsBib')
			f.write(str(i))
			f.write('\">\n')
			f.write('\t\t<mdWrap MDTYPE=\"MODS\" LABEL=\"Page metadata\">\n')
			f.write('\t\t\t<xmlData>\n')
			f.write('\t\t\t\t<mods:mods>\n')
			f.write('\t\t\t\t\t<mods:part>\n')
			f.write('\t\t\t\t\t\t<mods:extent unit=\"pages\">\n')
			f.write('\t\t\t\t\t\t\t<mods:start>')
			f.write(str(i))
			f.write('</mods:start>\n')
			f.write('\t\t\t\t\t\t</mods:extent>\n')
			f.write('\t\t\t\t\t\t<mods:detail type=\"page number\">\n')
			f.write('\t\t\t\t\t\t\t<mods:number>')
			f.write(str(i))
			f.write('</mods:number>\n')
			f.write('\t\t\t\t\t\t</mods:detail>\n')
			f.write('\t\t\t\t\t</mods:part>\n')
			f.write('\t\t\t\t\t<mods:relatedItem type=\"original\">\n')
			f.write('\t\t\t\t\t\t<mods:physicalDescription>\n')
			f.write('\t\t\t\t\t\t\t<mods:form type=\"print\"/>\n')
			f.write('\t\t\t\t\t\t</mods:physicalDescription>\n')
			f.write('\t\t\t\t\t\t<mods:location>\n')
			f.write('\t\t\t\t\t\t\t<mods:physicalLocation authority=\"marcorg\" displayLabel=\"Bayerische Staatsbibliothek\">demnbsb</mods:physicalLocation>\n')
			f.write('\t\t\t\t\t\t</mods:location>\n')
			f.write('\t\t\t\t\t</mods:relatedItem>\n')
			f.write('\t\t\t\t\t<mods:note type=\"agencyResponsibleForReproduction\" displayLabel=\"Bayerische Staatsbibliothek\">demnbsb</mods:note>\n')
			f.write('\t\t\t\t\t<mods:note type=\"noteAboutReproduction\">Present</mods:note>\n')
			f.write('\t\t\t\t</mods:mods>\n')
			f.write('\t\t\t</xmlData>\n')
			f.write('\t\t</mdWrap>\n')
			f.write('\t</dmdSec>\n')
		f.write('\t<!--FILE SECTION-->\n')
		f.write('\t<fileSec>\n')
		for i in range(1,num+1):
			if i<10:
				name = '000'+str(i)
			else:
				name = '00'+str(i)
			f.write('\t\t<fileGrp ID=\"pageFileGrp')
			f.write(str(i))
			f.write('\">\n')
			f.write('\t\t\t<file ID=\"masterFile')
			f.write(str(i))
			f.write('\" USE=\"master\">\n')
			f.write('\t\t\t\t<FLocat LOCTYPE=\"OTHER\" OTHERLOCTYPE=\"file\" xlink:href=\"')
			f.write(name)
			f.write('.tif\" />\n')
			f.write('\t\t\t</file>\n')
			f.write('\t\t\t<file ID=\"serviceFile')
			f.write(str(i))
			f.write('\" USE=\"service\">\n')
			f.write('\t\t\t\t<FLocat LOCTYPE=\"OTHER\" OTHERLOCTYPE=\"file\" xlink:href=\"')
			f.write(name)
			f.write('.jp2\" />\n')
			f.write('\t\t\t</file>\n')
			f.write('\t\t\t<file ID=\"otherDerivativeFile')
			f.write(str(i))
			f.write('\" USE=\"derivative\">\n')
			f.write('\t\t\t\t<FLocat LOCTYPE=\"OTHER\" OTHERLOCTYPE=\"file\" xlink:href=\"')
			f.write(name)
			f.write('.pdf\" />\n')
			f.write('\t\t\t</file>\n')
			f.write('\t\t\t<file ID=\"ocrFile')
			f.write(str(i))
			f.write('\" USE=\"ocr\">\n')
			f.write('\t\t\t\t<FLocat LOCTYPE=\"OTHER\" OTHERLOCTYPE=\"file\" xlink:href=\"')
			f.write(name)
			f.write('.xml\"/>\n')
			f.write('\t\t\t</file>\n')
			f.write('\t\t</fileGrp>\n')
		f.write('\t</fileSec>\n')
		f.write('\t<!--STRUCTURAL MAP-->\n')
		f.write('\t<structMap xmlns:np=\"urn:library-of-congress:ndnp:mets:newspaper\">\n')
		f.write('\t\t<div TYPE=\"np:issue\" DMDID=\"issueModsBib\">\n')
		for i in range(1,num+1):
			f.write('\t\t\t<div TYPE=\"np:page\" DMDID=\"pageModsBib')
			f.write(str(i))
			f.write('\">\n')
			f.write('\t\t\t\t<fptr FILEID=\"masterFile')
			f.write(str(i))
			f.write('\"/>\n')
			f.write('\t\t\t\t<fptr FILEID=\"serviceFile')
			f.write(str(i))
			f.write('\"/>\n')
			f.write('\t\t\t\t<fptr FILEID=\"otherDerivativeFile')
			f.write(str(i))
			f.write('\"/>\n')
			f.write('\t\t\t\t<fptr FILEID=\"ocrFile')
			f.write(str(i))
			f.write('\"/>\n')
			f.write('\t\t\t</div>\n')
		f.write('\t\t</div>\n')
		f.write('\t</structMap>\n')
		f.write('</mets>\n')

	with open(folder+"_1.xml","w",encoding="utf-8") as f:
		f.write('<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n')
		f.write('<mets xmlns=\"http://www.loc.gov/METS/\" xmlns:mix=\"http://www.loc.gov/mix/\" xmlns:mods=\"http://www.loc.gov/mods/v3\" xmlns:ndnp=\"http://www.loc.gov/ndnp\" xmlns:premis=\"http://www.oclc.org/premis\" xmlns:xlink=\"http://www.w3.org/1999/xlink\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" LABEL=\"Allgemeine Musikalische Zeitung, 1803-10-05\" PROFILE=\"urn:library-of-congress:mets:profiles:ndnp:issue:v1.5\" TYPE=\"urn:library-of-congress:ndnp:mets:newspaper:issue\" xsi:schemaLocation=\"\t  http://www.loc.gov/METS/ http://www.loc.gov/standards/mets/version17/mets.v1-7.xsd\t\thttp://www.loc.gov/mods/v3 http://www.loc.gov/standards/mods/v3/mods-3-3.xsd\">\n')
		f.write('<!--METS HEADER-->\n')
		f.write('<metsHdr ADMID=\"digSig\" CREATEDATE=\"')
		f.write(time)
		f.write('\" RECORDSTATUS=\"Validated\">\n')
		f.write('\t<agent ROLE=\"CREATOR\" TYPE=\"ORGANIZATION\">\n')
		f.write('\t\t<name>Bayerische Staatsbibliothek</name>\n')
		f.write('\t</agent>\n')
		f.write('</metsHdr>\n')

		f.write('<!--DESCRIPTIVE METADATA-->\n')

		f.write('<dmdSec ID=\"issueModsBib\">\n')
		f.write('\t<mdWrap LABEL=\"Issue metadata\" MDTYPE=\"MODS\">\n')
		f.write('\t\t<xmlData>\n')
		f.write('\t\t\t<mods:mods>\n')
		f.write('\t\t\t\t<mods:relatedItem type=\"host\">\n')
		f.write('\t\t\t\t\t<mods:identifier type=\"lccn\">BV002720696</mods:identifier>\n')
		f.write('\t\t\t\t\t<mods:part>\n')
		f.write('\t\t\t\t\t\t<mods:detail type=\"volume\">\n')
		f.write('\t\t\t\t\t\t\t<mods:number>')
		f.write(volume_num)
		f.write('</mods:number>\n')
		f.write('\t\t\t\t\t\t</mods:detail>\n')
		f.write('\t\t\t\t\t\t<mods:detail type=\"issue\">\n')
		f.write('\t\t\t\t\t\t\t<mods:number>')
		f.write(str(issue))
		f.write('</mods:number>\n')
		f.write('\t\t\t\t\t\t</mods:detail>\n')
		f.write('\t\t\t\t\t\t<mods:detail type=\"edition\">\n')
		f.write('\t\t\t\t\t\t\t<mods:number>1</mods:number>\n')
		f.write('\t\t\t\t\t\t</mods:detail>\n')
		f.write('\t\t\t\t\t</mods:part>\n')
		f.write('\t\t\t\t</mods:relatedItem>\n')
		f.write('\t\t\t\t<mods:originInfo>\n')
		f.write('\t\t\t\t\t<mods:dateIssued encoding=\"iso8601\">')
		f.write(volume[0:4])
		f.write('-')
		f.write(volume[4:6])
		f.write('-')
		f.write(volume[6:8])
		f.write('</mods:dateIssued>\n')
		f.write('\t\t\t\t</mods:originInfo>\n')
		f.write('\t\t\t\t<mods:note type=\"noteAboutReproduction\">Present</mods:note>\n')
		f.write('\t\t\t</mods:mods>\n')
		f.write('\t\t</xmlData>\n')
		f.write('\t</mdWrap>\n')
		f.write('</dmdSec>\n')

		for i in range(1,num+1):
			f.write('<dmdSec ID=\"pageModsBib')
			f.write(str(i))
			f.write('\">\n')
			f.write('\t<mdWrap LABEL=\"Page metadata\" MDTYPE=\"MODS\">\n')
			f.write('\t\t<xmlData>\n')
			f.write('\t\t\t<mods:mods>\n')
			f.write('\t\t\t\t<mods:part>\n')
			f.write('\t\t\t\t\t<mods:extent unit=\"pages\">\n')
			f.write('\t\t\t\t\t\t<mods:start>')
			f.write(str(i))
			f.write('</mods:start>\n')
			f.write('\t\t\t\t\t</mods:extent>\n')
			f.write('\t\t\t\t\t<mods:detail type=\"page number\">\n')
			f.write('\t\t\t\t\t\t<mods:number>')
			f.write(str(i))
			f.write('</mods:number>\n')
			f.write('\t\t\t\t\t</mods:detail>\n')
			f.write('\t\t\t\t</mods:part>\n')
			f.write('\t\t\t\t<mods:relatedItem type=\"original\">\n')
			f.write('\t\t\t\t\t<mods:physicalDescription>\n')
			f.write('\t\t\t\t\t\t<mods:form type=\"print\"/>\n')
			f.write('\t\t\t\t\t</mods:physicalDescription>\n')
			f.write('\t\t\t\t\t<mods:location>\n')
			f.write('\t\t\t\t\t\t<mods:physicalLocation authority=\"marcorg\" displayLabel=\"Bayerische Staatsbibliothek\">demnbsb</mods:physicalLocation>\n')
			f.write('\t\t\t\t\t</mods:location>\n')
			f.write('\t\t\t\t</mods:relatedItem>\n')
			f.write('\t\t\t\t<mods:note displayLabel=\"Bayerische Staatsbibliothek\" type=\"agencyResponsibleForReproduction\">demnbsb</mods:note>\n')
			f.write('\t\t\t\t<mods:note type=\"noteAboutReproduction\">Present</mods:note>\n')
			f.write('\t\t\t</mods:mods>\n')
			f.write('\t\t</xmlData>\n')
			f.write('\t</mdWrap>\n')
			f.write('</dmdSec>\n')

		f.write('<amdSec>\n')

		for i in range(1,num+1):
			f.write('\t<techMD ID=\"mixmasterFile')
			f.write(str(i))
			f.write('\">\n')
			f.write('\t\t<mdWrap LABEL=\"NISO still image metadata\" MDTYPE=\"NISOIMG\">\n')
			f.write('\t\t\t<xmlData>\n')
			f.write('\t\t\t\t<mix:mix>\n')
			f.write('\t\t\t\t\t<mix:BasicImageParameters>\n')
			f.write('\t\t\t\t\t\t<mix:Format>\n')
			f.write('\t\t\t\t\t\t\t<mix:Compression>\n')
			f.write('\t\t\t\t\t\t\t\t<mix:CompressionScheme>1</mix:CompressionScheme>\n')
			f.write('\t\t\t\t\t\t\t</mix:Compression>\n')
			f.write('\t\t\t\t\t\t\t<mix:PhotometricInterpretation>\n')
			f.write('\t\t\t\t\t\t\t\t<mix:ColorSpace>1</mix:ColorSpace>\n')
			f.write('\t\t\t\t\t\t\t</mix:PhotometricInterpretation>\n')
			f.write('\t\t\t\t\t\t</mix:Format>\n')
			f.write('\t\t\t\t\t</mix:BasicImageParameters>\n')
			f.write('\t\t\t\t\t<mix:ImageCreation>\n')
			f.write('\t\t\t\t\t\t<mix:SourceType>print</mix:SourceType>\n')
			f.write('\t\t\t\t\t\t<mix:ImageProducer>Bayerische Staatsbibliothek; iArchives</mix:ImageProducer>\n')
			f.write('\t\t\t\t\t\t<mix:ScanningSystemCapture>\n')
			f.write('\t\t\t\t\t\t\t<mix:ScanningSystemHardware>\n')
			f.write('\t\t\t\t\t\t\t\t<mix:ScannerManufacturer>Canon</mix:ScannerManufacturer>\n')
			f.write('\t\t\t\t\t\t\t\t<mix:ScannerModel>\n')
			f.write('\t\t\t\t\t\t\t\t\t<mix:ScannerModelName>EOS-1DS,SN# 109662</mix:ScannerModelName>\n')
			f.write('\t\t\t\t\t\t\t\t</mix:ScannerModel>\n')
			f.write('\t\t\t\t\t\t\t</mix:ScanningSystemHardware>\n')
			f.write('\t\t\t\t\t\t</mix:ScanningSystemCapture>\n')
			f.write('\t\t\t\t\t</mix:ImageCreation>\n')
			f.write('\t\t\t\t\t<mix:ImagingPerformanceAssessment>\n')
			f.write('\t\t\t\t\t\t<mix:SpatialMetrics>\n')
			f.write('\t\t\t\t\t\t\t<mix:SamplingFrequencyUnit>2</mix:SamplingFrequencyUnit>\n')
			f.write('\t\t\t\t\t\t\t<mix:XSamplingFrequency>400</mix:XSamplingFrequency>\n')
			f.write('\t\t\t\t\t\t\t<mix:YSamplingFrequency>400</mix:YSamplingFrequency>\n')
			f.write('\t\t\t\t\t\t\t<mix:ImageWidth>6543</mix:ImageWidth>\n')
			f.write('\t\t\t\t\t\t\t<mix:ImageLength>8736</mix:ImageLength>\n')
			f.write('\t\t\t\t\t\t</mix:SpatialMetrics>\n')
			f.write('\t\t\t\t\t\t<mix:Energetics>\n')
			f.write('\t\t\t\t\t\t\t<mix:BitsPerSample>8</mix:BitsPerSample>\n')
			f.write('\t\t\t\t\t\t</mix:Energetics>\n')
			f.write('\t\t\t\t\t</mix:ImagingPerformanceAssessment>\n')
			f.write('\t\t\t\t</mix:mix>\n')
			f.write('\t\t\t</xmlData>\n')
			f.write('\t\t</mdWrap>\n')
			f.write('\t</techMD>\n')
			f.write('\t<techMD ID=\"premismasterFile')
			f.write(str(i))
			f.write('\">\n')
			f.write('\t\t<mdWrap LABEL=\"PREMIS object metadata\" MDTYPE=\"OTHER\" OTHERMDTYPE=\"PREMIS\">\n')
			f.write('\t\t\t<xmlData>\n')
			f.write('\t\t\t\t<premis:object xmlns:premis=\"http://www.loc.gov/standards/premis\">\n')
			f.write('\t\t\t\t\t<premis:objectCharacteristics>\n')
			f.write('\t\t\t\t\t\t<premis:fixity>\n')
			f.write('\t\t\t\t\t\t\t<premis:messageDigestAlgorithm>SHA-1</premis:messageDigestAlgorithm>\n')
			f.write('\t\t\t\t\t\t\t<premis:messageDigest>ab815d2ce14cefadcf57229cd03928928eaca2dc</premis:messageDigest>\n')
			f.write('\t\t\t\t\t\t\t<premis:messageDigestOriginator>Library of Congress</premis:messageDigestOriginator>\n')
			f.write('\t\t\t\t\t\t</premis:fixity>\n')
			f.write('\t\t\t\t\t\t<premis:size>57160218</premis:size>\n')
			f.write('\t\t\t\t\t\t<premis:format>\n')
			f.write('\t\t\t\t\t\t\t<premis:formatDesignation>\n')
			f.write('\t\t\t\t\t\t\t\t<premis:formatName>image/tiff</premis:formatName>\n')
			f.write('\t\t\t\t\t\t\t</premis:formatDesignation>\n')
			f.write('\t\t\t\t\t\t</premis:format>\n')
			f.write('\t\t\t\t\t</premis:objectCharacteristics>\n')
			f.write('\t\t\t\t\t<premis:creatingApplication>\n')
			f.write('\t\t\t\t\t\t<premis:creatingApplicationName>iArchives, Inc., 3.318</premis:creatingApplicationName>\n')
			f.write('\t\t\t\t\t\t<premis:dateCreatedByApplication>2012-02-21T11:22:58</premis:dateCreatedByApplication>\n')
			f.write('\t\t\t\t\t</premis:creatingApplication>\n')
			f.write('\t\t\t\t</premis:object>\n')
			f.write('\t\t\t</xmlData>\n')
			f.write('\t\t</mdWrap>\n')
			f.write('\t</techMD>\n')
			f.write('\t<techMD ID=\"mixserviceFile')
			f.write(str(i))
			f.write('\">\n')
			f.write('\t\t<mdWrap LABEL=\"NISO still image metadata\" MDTYPE=\"NISOIMG\">\n')
			f.write('\t\t\t<xmlData>\n')
			f.write('\t\t\t\t<mix:mix>\n')
			f.write('\t\t\t\t\t<mix:BasicImageParameters>\n')
			f.write('\t\t\t\t\t\t<mix:Format>\n')
			f.write('\t\t\t\t\t\t\t<mix:Compression>\n')
			f.write('\t\t\t\t\t\t\t\t<mix:CompressionScheme>34712</mix:CompressionScheme>\n')
			f.write('\t\t\t\t\t\t\t</mix:Compression>\n')
			f.write('\t\t\t\t\t\t</mix:Format>\n')
			f.write('\t\t\t\t\t</mix:BasicImageParameters>\n')
			f.write('\t\t\t\t\t<mix:ImageCreation/>\n')
			f.write('\t\t\t\t\t<mix:ImagingPerformanceAssessment>\n')
			f.write('\t\t\t\t\t\t<mix:SpatialMetrics>\n')
			f.write('\t\t\t\t\t\t\t<mix:ImageWidth>6544</mix:ImageWidth>\n')
			f.write('\t\t\t\t\t\t\t<mix:ImageLength>8736</mix:ImageLength>\n')
			f.write('\t\t\t\t\t\t</mix:SpatialMetrics>\n')
			f.write('\t\t\t\t\t\t<mix:Energetics>\n')
			f.write('\t\t\t\t\t\t\t<mix:BitsPerSample>8</mix:BitsPerSample>\n')
			f.write('\t\t\t\t\t\t</mix:Energetics>\n')
			f.write('\t\t\t\t\t</mix:ImagingPerformanceAssessment>\n')
			f.write('\t\t\t\t</mix:mix>\n')
			f.write('\t\t\t</xmlData>\n')
			f.write('\t\t</mdWrap>\n')
			f.write('\t</techMD>\n')
			f.write('\t<techMD ID=\"premisserviceFile')
			f.write(str(i))
			f.write('\">\n')
			f.write('\t\t<mdWrap LABEL=\"PREMIS object metadata\" MDTYPE=\"OTHER\" OTHERMDTYPE=\"PREMIS\">\n')
			f.write('\t\t\t<xmlData>\n')
			f.write('\t\t\t\t<premis:object xmlns:premis=\"http://www.loc.gov/standards/premis\">\n')
			f.write('\t\t\t\t\t<premis:objectCharacteristics>\n')
			f.write('\t\t\t\t\t\t<premis:fixity>\n')
			f.write('\t\t\t\t\t\t\t<premis:messageDigestAlgorithm>SHA-1</premis:messageDigestAlgorithm>\n')
			f.write('\t\t\t\t\t\t\t<premis:messageDigest>dc82e4e9380377e447e6dbc64d85e826aa9381f4</premis:messageDigest>\n')
			f.write('\t\t\t\t\t\t\t<premis:messageDigestOriginator>Library of Congress</premis:messageDigestOriginator>\n')
			f.write('\t\t\t\t\t\t</premis:fixity>\n')
			f.write('\t\t\t\t\t\t<premis:size>7147099</premis:size>\n')
			f.write('\t\t\t\t\t\t<premis:format>\n')
			f.write('\t\t\t\t\t\t\t<premis:formatDesignation>\n')
			f.write('\t\t\t\t\t\t\t\t<premis:formatName>image/jp2</premis:formatName>\n')
			f.write('\t\t\t\t\t\t\t</premis:formatDesignation>\n')
			f.write('\t\t\t\t\t\t</premis:format>\n')
			f.write('\t\t\t\t\t</premis:objectCharacteristics>\n')
			f.write('\t\t\t\t\t<premis:creatingApplication/>\n')
			f.write('\t\t\t\t</premis:object>\n')
			f.write('\t\t\t</xmlData>\n')
			f.write('\t\t</mdWrap>\n')
			f.write('\t</techMD>\n')
			f.write('\t<techMD ID=\"premisotherDerivativeFile')
			f.write(str(i))
			f.write('\">\n')
			f.write('\t\t<mdWrap LABEL=\"PREMIS object metadata\" MDTYPE=\"OTHER\" OTHERMDTYPE=\"PREMIS\">\n')
			f.write('\t\t\t<xmlData>\n')
			f.write('\t\t\t\t<premis:object xmlns:premis=\"http://www.loc.gov/standards/premis\">\n')
			f.write('\t\t\t\t\t<premis:objectCharacteristics>\n')
			f.write('\t\t\t\t\t\t<premis:fixity>\n')
			f.write('\t\t\t\t\t\t\t<premis:messageDigestAlgorithm>SHA-1</premis:messageDigestAlgorithm>\n')
			f.write('\t\t\t\t\t\t\t<premis:messageDigest>237acb2984825911a78db9d9682ad12da59a965e</premis:messageDigest>\n')
			f.write('\t\t\t\t\t\t\t<premis:messageDigestOriginator>Library of Congress</premis:messageDigestOriginator>\n')
			f.write('\t\t\t\t\t\t</premis:fixity>\n')
			f.write('\t\t\t\t\t\t<premis:size>794497</premis:size>\n')
			f.write('\t\t\t\t\t\t<premis:format>\n')
			f.write('\t\t\t\t\t\t\t<premis:formatDesignation>\n')
			f.write('\t\t\t\t\t\t\t\t<premis:formatName>application/pdf</premis:formatName>\n')
			f.write('\t\t\t\t\t\t\t</premis:formatDesignation>\n')
			f.write('\t\t\t\t\t\t</premis:format>\n')
			f.write('\t\t\t\t\t</premis:objectCharacteristics>\n')
			f.write('\t\t\t\t\t<premis:creatingApplication>\n')
			f.write('\t\t\t\t\t\t<premis:dateCreatedByApplication>2012-01-06T07:59:14</premis:dateCreatedByApplication>\n')
			f.write('\t\t\t\t\t</premis:creatingApplication>\n')
			f.write('\t\t\t\t</premis:object>\n')
			f.write('\t\t\t</xmlData>\n')
			f.write('\t\t</mdWrap>\n')
			f.write('\t</techMD>\n')
			f.write('\t<techMD ID=\"premisocrFile')
			f.write(str(i))
			f.write('\">\n')
			f.write('\t\t<mdWrap LABEL=\"PREMIS object metadata\" MDTYPE=\"OTHER\" OTHERMDTYPE=\"PREMIS\">\n')
			f.write('\t\t\t<xmlData>\n')
			f.write('\t\t\t\t<premis:object xmlns:premis=\"http://www.loc.gov/standards/premis\">\n')
			f.write('\t\t\t\t\t<premis:objectCharacteristics>\n')
			f.write('\t\t\t\t\t\t<premis:fixity>\n')
			f.write('\t\t\t\t\t\t\t<premis:messageDigestAlgorithm>SHA-1</premis:messageDigestAlgorithm>\n')
			f.write('\t\t\t\t\t\t\t<premis:messageDigest>f471f13af3c125813098f7f907c46e5468758f9e</premis:messageDigest>\n')
			f.write('\t\t\t\t\t\t\t<premis:messageDigestOriginator>Library of Congress</premis:messageDigestOriginator>\n')
			f.write('\t\t\t\t\t\t</premis:fixity>\n')
			f.write('\t\t\t\t\t\t<premis:size>1057150</premis:size>\n')
			f.write('\t\t\t\t\t\t<premis:format>\n')
			f.write('\t\t\t\t\t\t\t<premis:formatDesignation>\n')
			f.write('\t\t\t\t\t\t\t\t<premis:formatName>text/xml</premis:formatName>\n')
			f.write('\t\t\t\t\t\t\t</premis:formatDesignation>\n')
			f.write('\t\t\t\t\t\t</premis:format>\n')
			f.write('\t\t\t\t\t</premis:objectCharacteristics>\n')
			f.write('\t\t\t\t\t<premis:creatingApplication>\n')
			f.write('\t\t\t\t\t\t<premis:creatingApplicationName>iArchives iArchives OCR Framework Multiple</premis:creatingApplicationName>\n')
			f.write('\t\t\t\t\t</premis:creatingApplication>\n')
			f.write('\t\t\t\t</premis:object>\n')
			f.write('\t\t\t</xmlData>\n')
			f.write('\t\t</mdWrap>\n')
			f.write('\t</techMD>\n')

		f.write('\t<digiprovMD ID=\"digSig\">\n')
		f.write('\t\t<mdWrap LABEL=\"Mets record validation signature\" MDTYPE=\"OTHER\" OTHERMDTYPE=\"XML-Signature\">\n')
		f.write('\t\t\t<xmlData>\n')
		f.write('\t\t\t\t<Signature xmlns=\"http://www.w3.org/2000/09/xmldsig#\">\n')
		f.write('\t\t\t\t\t<SignedInfo>\n')
		f.write('\t\t\t\t\t\t<CanonicalizationMethod Algorithm=\"http://www.w3.org/TR/2001/REC-xml-c14n-20010315#WithComments\"/>\n')
		f.write('\t\t\t\t\t\t<SignatureMethod Algorithm=\"http://www.w3.org/2000/09/xmldsig#dsa-sha1\"/>\n')
		f.write('\t\t\t\t\t\t<Reference URI=\"\">\n')
		f.write('\t\t\t\t\t\t\t<Transforms>\n')
		f.write('\t\t\t\t\t\t\t\t<Transform Algorithm=\"http://www.w3.org/2000/09/xmldsig#enveloped-signature\"/>\n')
		f.write('\t\t\t\t\t\t\t</Transforms>\n')
		f.write('\t\t\t\t\t\t\t<DigestMethod Algorithm=\"http://www.w3.org/2000/09/xmldsig#sha1\"/>\n')
		f.write('\t\t\t\t\t\t\t<DigestValue>UgyYiGxyGHYyXxdnu2+aNIQJtfI=</DigestValue>\n')
		f.write('\t\t\t\t\t\t</Reference>\n')
		f.write('\t\t\t\t\t</SignedInfo>\n')
		f.write('\t\t\t\t\t<SignatureValue>OoEmomkS+wGjD3Ckg1H36W7z62dcUD4C0FjHM53/NE07urgFUBGFag==</SignatureValue>\n')
		f.write('\t\t\t\t\t<KeyInfo>\n')
		f.write('\t\t\t\t\t\t<KeyValue>\n')
		f.write('\t\t\t\t\t\t\t<DSAKeyValue>\n')
		f.write('\t\t\t\t\t\t\t\t<P>/X9TgR11EilS30qcLuzk5/YRt1I870QAwx4/gLZRJmlFXUAiUftZPY1Y+r/F9bow9subVWzXgTuA\n')
		f.write('\t\t\t\t\t\t\t\tHTRv8mZgt2uZUKWkn5/oBHsQIsJPu6nX/rfGG/g7V+fGqKYVDwT7g/bTxR7DAjVUE1oWkTL2dfOu\n')
		f.write('\t\t\t\t\t\t\t\tK2HXKu/yIgMZndFIAcc=</P>\n')
		f.write('\t\t\t\t\t\t\t\t<Q>l2BQjxUjC8yykrmCouuEC/BYHPU=</Q>\n')
		f.write('\t\t\t\t\t\t\t\t<G>9+GghdabPd7LvKtcNrhXuXmUr7v6OuqC+VdMCz0HgmdRWVeOutRZT+ZxBxCBgLRJFnEj6EwoFhO3\n')
		f.write('\t\t\t\t\t\t\t\tzwkyjMim4TwWeotUfI0o4KOuHiuzpnWRbqN/C/ohNWLx+2J6ASQ7zKTxvqhRkImog9/hWuWfBpKL\n')
		f.write('\t\t\t\t\t\t\t\tZl6Ae1UlZAFMO/7PSSo=</G>\n')
		f.write('\t\t\t\t\t\t\t\t<Y>f/O4UPVRVYtDd9XkWVAV7Oq8eB8lksfUstddlqkowbmQ4m9FPX1y03czYMfHwJBm9xIaQmHioJHO\n')
		f.write('\t\t\t\t\t\t\t\tucRqLI+R4ntFuCqYuh+p65IpZH5SbN5b3iZTEUm+Gz1g4aKDJarstd2aAvOmaifzVY/75ylbROoP\n')
		f.write('\t\t\t\t\t\t\t\t7lKsd/ifES8XcHXUHlU=</Y>\n')
		f.write('\t\t\t\t\t\t\t</DSAKeyValue>\n')
		f.write('\t\t\t\t\t\t</KeyValue>\n')
		f.write('\t\t\t\t\t\t<KeyName>NDNP.3.13</KeyName>\n')
		f.write('\t\t\t\t\t</KeyInfo>\n')
		f.write('\t\t\t\t</Signature>\n')
		f.write('\t\t\t</xmlData>\n')
		f.write('\t\t</mdWrap>\n')
		f.write('\t</digiprovMD>\n')

		f.write('</amdSec>\n')

		f.write('<!--FILE SECTION-->\n')
		f.write('<fileSec>\n')

		for i in range(1,num+1):
			if i<10:
				name = '000'+str(i)
			else:
				name = '00'+str(i)
			f.write('\t<fileGrp ID=\"pageFileGrp')
			f.write(str(i))
			f.write('\">\n')
			f.write('\t\t<file ADMID=\"mixmasterFile')
			f.write(str(i))
			f.write(' premismasterFile')
			f.write(str(i))
			f.write('\" ID=\"masterFile')
			f.write(str(i))
			f.write('\" USE=\"master\">\n')
			f.write('\t\t\t<FLocat LOCTYPE=\"OTHER\" OTHERLOCTYPE=\"file\" xlink:href=\"')
			f.write(name)
			f.write('.tif\"/>\n')
			f.write('\t\t</file>\n')
			f.write('\t\t<file ADMID=\"mixserviceFile')
			f.write(str(i))
			f.write(' premisserviceFile')
			f.write(str(i))
			f.write('\" ID=\"serviceFile')
			f.write(str(i))
			f.write('\" USE=\"service\">\n')
			f.write('\t\t\t<FLocat LOCTYPE=\"OTHER\" OTHERLOCTYPE=\"file\" xlink:href=\"')
			f.write(name)
			f.write('.jp2\"/>\n')
			f.write('\t\t</file>\n')
			f.write('\t\t<file ADMID=\"premisotherDerivativeFile')
			f.write(str(i))
			f.write('\" ID=\"otherDerivativeFile')
			f.write(str(i))
			f.write('\" USE=\"derivative\">\n')
			f.write('\t\t\t<FLocat LOCTYPE=\"OTHER\" OTHERLOCTYPE=\"file\" xlink:href=\"')
			f.write(name)
			f.write('.pdf\"/>\n')
			f.write('\t\t</file>\n')
			f.write('\t\t<file ADMID=\"premisocrFile')
			f.write(str(i))
			f.write('\" ID=\"ocrFile')
			f.write(str(i))
			f.write('\" USE=\"ocr\">\n')
			f.write('\t\t\t<FLocat LOCTYPE=\"OTHER\" OTHERLOCTYPE=\"file\" xlink:href=\"')
			f.write(name)
			f.write('.xml\"/>\n')
			f.write('\t\t</file>\n')
			f.write('\t</fileGrp>\n')

		f.write('</fileSec>\n')

		f.write('<!--STRUCTURAL MAP-->\n')
		f.write('<structMap xmlns:np=\"urn:library-of-congress:ndnp:mets:newspaper\">\n')
		f.write('\t<div DMDID=\"issueModsBib\" TYPE=\"np:issue\">\n')

		f.write('\t\t<div DMDID=\"pageModsBib')
		f.write(str(i))
		f.write('\" TYPE=\"np:page\">\n')
		f.write('\t\t\t<fptr FILEID=\"masterFile')
		f.write(str(i))
		f.write('\"/>\n')
		f.write('\t\t\t<fptr FILEID=\"serviceFile')
		f.write(str(i))
		f.write('\"/>\n')
		f.write('\t\t\t<fptr FILEID=\"otherDerivativeFile')
		f.write(str(i))
		f.write('\"/>\n')
		f.write('\t\t\t<fptr FILEID=\"ocrFile')
		f.write(str(i))
		f.write('\"/>\n')
		f.write('\t\t</div>\n')

		f.write('\t</div>\n')
		f.write('</structMap>\n')
		f.write('</mets>\n')

	os.chdir("..")

with open("../../batch.xml","a",encoding="utf-8") as f:
	f.write('</ndnp:batch>')
with open("../../batch_1.xml","a",encoding="utf-8") as f:
	f.write('</ndnp:batch>')