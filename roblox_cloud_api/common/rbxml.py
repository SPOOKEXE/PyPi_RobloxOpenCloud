
import xml.etree.ElementTree as ET

from typing import Callable

WHITELISED_XML_INDEXES = ["Item", "Properties"]

class XMLFile:

	'''
	Follow the given path in the XML tree
	'''
	@staticmethod
	def follow_path( parent : ET.Element, path : list[int] ) -> ET.Element:
		for step in path:
			parent = parent[step]
		return parent

	'''
	Attempt to find an attribute in the xml element
	'''
	@staticmethod
	def get_attribute(properties : ET.Element, key : str) -> ET.Element:
		for prop in list(properties.iter()):
			if prop.attrib.get("name") == key:
				return prop

class RobloxXML:

	'''
	Recursively search the XML tree for the Items/Properties
	that roblox utilizes in their XML data.
	'''
	@staticmethod
	def recursive_search(parent : ET.Element, path=None, items=None) -> list[list[ET.Element, list[int]]]:
		if path == None: path = []
		if items == None: items = []

		children = []
		for value in WHITELISED_XML_INDEXES:
			children.extend( parent.findall(value) )

		for i, child in enumerate(children):
			if WHITELISED_XML_INDEXES.count(child.tag) > 0:
				new_path = path.copy()
				new_path.append(i)
				items.append([child, new_path])
				RobloxXML.recursive_search( child, path=new_path, items=items )
		return items

	'''
	Recursively search but calls the callback with any Item/Properties node that was found.
	'''
	@staticmethod
	def recursive_node_callback( tree : ET.ElementTree, callback : Callable ) -> None:
		for data in RobloxXML.recursive_search( tree.getroot() ):
			node, _ = tuple( data )
			callback( node )
