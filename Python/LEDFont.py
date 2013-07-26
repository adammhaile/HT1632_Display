class LEDFont:
	_index_list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 0]
	
	_width_list = [1, 1, 3, 5, 5, 7, 5, 1, 3, 3, 5, 5, 2, 5, 1, 5, 5, 3, 5, 5, 5, 5, 5, 5, 5, 5, 1, 2, 4, 5, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 3, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 3, 5, 3, 5, 5, 3, 5, 5, 5, 5, 5, 5, 5, 5, 3, 4, 5, 3, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 1, 5, 5]
	
	_font = [
	  [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],
	  [0xfa, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],
	  [0xe0, 0x00, 0xe0, 0x00, 0x00, 0x00, 0x00, 0x00],
	  [0x28, 0xfe, 0x28, 0xfe, 0x28, 0x00, 0x00, 0x00],
	  [0x24, 0x54, 0xfe, 0x54, 0x48, 0x00, 0x00, 0x00],
	  [0xc0, 0xc4, 0x08, 0x10, 0x20, 0x46, 0x06, 0x00],
	  [0x6c, 0x92, 0x6a, 0x04, 0x0a, 0x00, 0x00, 0x00],
	  [0xe0, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],
	  [0x38, 0x44, 0x82, 0x00, 0x00, 0x00, 0x00, 0x00],
	  [0x82, 0x44, 0x38, 0x00, 0x00, 0x00, 0x00, 0x00],
	  [0x44, 0x28, 0xfe, 0x28, 0x44, 0x00, 0x00, 0x00],
	  [0x10, 0x10, 0x7c, 0x10, 0x10, 0x00, 0x00, 0x00],
	  [0x01, 0x06, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],
	  [0x10, 0x10, 0x10, 0x10, 0x10, 0x00, 0x00, 0x00],
	  [0x02, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],
	  [0x04, 0x08, 0x10, 0x20, 0x40, 0x00, 0x00, 0x00],
	  [0x7c, 0x8a, 0x92, 0xa2, 0x7c, 0x00, 0x00, 0x00],
	  [0x42, 0xfe, 0x02, 0x00, 0x00, 0x00, 0x00, 0x00],
	  [0x46, 0x8a, 0x92, 0x92, 0x62, 0x00, 0x00, 0x00],
	  [0x84, 0x82, 0x92, 0xb2, 0xcc, 0x00, 0x00, 0x00],
	  [0x18, 0x28, 0x48, 0xfe, 0x08, 0x00, 0x00, 0x00],
	  [0xe4, 0xa2, 0xa2, 0xa2, 0x9c, 0x00, 0x00, 0x00],
	  [0x3c, 0x52, 0x92, 0x92, 0x8c, 0x00, 0x00, 0x00],
	  [0x80, 0x8e, 0x90, 0xa0, 0xc0, 0x00, 0x00, 0x00],
	  [0x6c, 0x92, 0x92, 0x92, 0x6c, 0x00, 0x00, 0x00],
	  [0x62, 0x92, 0x92, 0x94, 0x78, 0x00, 0x00, 0x00],
	  [0x14, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],
	  [0x01, 0x16, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],
	  [0x10, 0x28, 0x44, 0x82, 0x00, 0x00, 0x00, 0x00],
	  [0x28, 0x28, 0x28, 0x28, 0x28, 0x00, 0x00, 0x00],
	  [0x82, 0x44, 0x28, 0x10, 0x00, 0x00, 0x00, 0x00],
	  [0x40, 0x80, 0x9a, 0xa0, 0x40, 0x00, 0x00, 0x00],
	  [0x7c, 0x82, 0xba, 0x9a, 0x72, 0x00, 0x00, 0x00],
	  [0x3e, 0x48, 0x88, 0x48, 0x3e, 0x00, 0x00, 0x00],
	  [0xfe, 0x92, 0x92, 0x92, 0x6c, 0x00, 0x00, 0x00],
	  [0x7c, 0x82, 0x82, 0x82, 0x44, 0x00, 0x00, 0x00],
	  [0xfe, 0x82, 0x82, 0x82, 0x7c, 0x00, 0x00, 0x00],
	  [0xfe, 0x92, 0x92, 0x92, 0x82, 0x00, 0x00, 0x00],
	  [0xfe, 0x90, 0x90, 0x90, 0x80, 0x00, 0x00, 0x00],
	  [0x7c, 0x82, 0x82, 0x8a, 0x8e, 0x00, 0x00, 0x00],
	  [0xfe, 0x10, 0x10, 0x10, 0xfe, 0x00, 0x00, 0x00],
	  [0x82, 0xfe, 0x82, 0x00, 0x00, 0x00, 0x00, 0x00],
	  [0x04, 0x02, 0x02, 0x02, 0xfc, 0x00, 0x00, 0x00],
	  [0xfe, 0x10, 0x28, 0x44, 0x82, 0x00, 0x00, 0x00],
	  [0xfe, 0x02, 0x02, 0x02, 0x02, 0x00, 0x00, 0x00],
	  [0xfe, 0x40, 0x30, 0x40, 0xfe, 0x00, 0x00, 0x00],
	  [0xfe, 0x20, 0x10, 0x08, 0xfe, 0x00, 0x00, 0x00],
	  [0x7c, 0x82, 0x82, 0x82, 0x7c, 0x00, 0x00, 0x00],
	  [0xfe, 0x90, 0x90, 0x90, 0x60, 0x00, 0x00, 0x00],
	  [0x7c, 0x82, 0x8a, 0x84, 0x7a, 0x00, 0x00, 0x00],
	  [0xfe, 0x90, 0x98, 0x94, 0x62, 0x00, 0x00, 0x00],
	  [0x64, 0x92, 0x92, 0x92, 0x4c, 0x00, 0x00, 0x00],
	  [0x80, 0x80, 0xfe, 0x80, 0x80, 0x00, 0x00, 0x00],
	  [0xfc, 0x02, 0x02, 0x02, 0xfc, 0x00, 0x00, 0x00],
	  [0xf8, 0x04, 0x02, 0x04, 0xf8, 0x00, 0x00, 0x00],
	  [0xfe, 0x04, 0x18, 0x04, 0xfe, 0x00, 0x00, 0x00],
	  [0xc6, 0x28, 0x10, 0x28, 0xc6, 0x00, 0x00, 0x00],
	  [0xc0, 0x20, 0x1e, 0x20, 0xc0, 0x00, 0x00, 0x00],
	  [0x86, 0x8a, 0x92, 0xa2, 0xc2, 0x00, 0x00, 0x00],
	  [0xfe, 0x82, 0x82, 0x00, 0x00, 0x00, 0x00, 0x00],
	  [0x40, 0x20, 0x10, 0x08, 0x04, 0x00, 0x00, 0x00],
	  [0x82, 0x82, 0xfe, 0x00, 0x00, 0x00, 0x00, 0x00],
	  [0x10, 0x20, 0x40, 0x20, 0x10, 0x00, 0x00, 0x00],
	  [0x02, 0x02, 0x02, 0x02, 0x02, 0x00, 0x00, 0x00],
	  [0x80, 0x40, 0x20, 0x00, 0x00, 0x00, 0x00, 0x00],
	  [0x04, 0x2a, 0x2a, 0x2a, 0x1e, 0x00, 0x00, 0x00],
	  [0xfe, 0x22, 0x22, 0x22, 0x1c, 0x00, 0x00, 0x00],
	  [0x1c, 0x22, 0x22, 0x22, 0x22, 0x00, 0x00, 0x00],
	  [0x1c, 0x22, 0x22, 0x22, 0xfe, 0x00, 0x00, 0x00],
	  [0x1c, 0x2a, 0x2a, 0x2a, 0x1a, 0x00, 0x00, 0x00],
	  [0x10, 0x7e, 0x90, 0x90, 0x40, 0x00, 0x00, 0x00],
	  [0x18, 0x25, 0x25, 0x25, 0x1e, 0x00, 0x00, 0x00],
	  [0xfe, 0x20, 0x20, 0x20, 0x1e, 0x00, 0x00, 0x00],
	  [0x22, 0xbe, 0x02, 0x00, 0x00, 0x00, 0x00, 0x00],
	  [0x02, 0x01, 0x21, 0xbe, 0x00, 0x00, 0x00, 0x00],
	  [0xfe, 0x08, 0x08, 0x14, 0x22, 0x00, 0x00, 0x00],
	  [0x82, 0xfe, 0x02, 0x00, 0x00, 0x00, 0x00, 0x00],
	  [0x3e, 0x20, 0x18, 0x20, 0x3e, 0x00, 0x00, 0x00],
	  [0x3e, 0x20, 0x20, 0x20, 0x1e, 0x00, 0x00, 0x00],
	  [0x1c, 0x22, 0x22, 0x22, 0x1c, 0x00, 0x00, 0x00],
	  [0x7f, 0x44, 0x44, 0x44, 0x38, 0x00, 0x00, 0x00],
	  [0x38, 0x44, 0x44, 0x44, 0x7f, 0x00, 0x00, 0x00],
	  [0x3e, 0x10, 0x20, 0x20, 0x20, 0x00, 0x00, 0x00],
	  [0x12, 0x2a, 0x2a, 0x2a, 0x24, 0x00, 0x00, 0x00],
	  [0x20, 0xfc, 0x22, 0x22, 0x04, 0x00, 0x00, 0x00],
	  [0x3c, 0x02, 0x02, 0x04, 0x3e, 0x00, 0x00, 0x00],
	  [0x38, 0x04, 0x02, 0x04, 0x38, 0x00, 0x00, 0x00],
	  [0x3e, 0x02, 0x0c, 0x02, 0x3e, 0x00, 0x00, 0x00],
	  [0x22, 0x14, 0x08, 0x14, 0x22, 0x00, 0x00, 0x00],
	  [0x38, 0x05, 0x05, 0x05, 0x3e, 0x00, 0x00, 0x00],
	  [0x22, 0x26, 0x2a, 0x32, 0x22, 0x00, 0x00, 0x00],
	  [0x10, 0x7c, 0xee, 0x82, 0x82, 0x00, 0x00, 0x00],
	  [0xfe, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],
	  [0x82, 0x82, 0xee, 0x7c, 0x10, 0x00, 0x00, 0x00],
	  [0x40, 0x80, 0xc0, 0x40, 0x80, 0x00, 0x00, 0x00],
	]

	def getCharData(self, char):
		i = self._index_list[ord(char)]
		return self._font[i]
		
	def getCharWidth(self, char):
		i = self._index_list[ord(char)]
		return self._width_list[i]