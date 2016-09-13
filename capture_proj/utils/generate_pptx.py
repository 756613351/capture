# #coding=utf8
# __author__ = 'lhp'
#
# import datetime
# import StringIO
#
# from pptx import Presentation
# from pptx.util import Inches
#
#
# class PPT(object):
#
#     max_width = 9
#     max_height = 4
#     min_top = 2.5
#     min_left = 0.5
#
#     def __init__(self):
#
#         self.ppt = Presentation('temp.pptx')
#         self.now_date = '{:%Y%m%d %H:%M}'.format(datetime.datetime.today())
#
#     def slide1(self, param):
#
#         slide = self.ppt.slides[1]
#         slide.shapes[3].table.rows[1].cells[0].textframe.text = param['text']
#
#     def slide_format(self, idx, param):
#         self.table_text_format(self.ppt.slides[idx].shapes[2].table, param['status'])
#         self.table_pic_format(self.ppt.slides[idx].shapes[4].table, param['pics'])
#
#     def table_text_format(self, table, status_text):
#         table.rows[1].cells[1].textframe.text = user[2]
#         table.rows[1].cells[3].textframe.text = self.now_date
#         table.rows[2].cells[1].textframe.text = status_text
#
#     def table_pic_format(self, table, image_dicts):
#         print datetime.datetime.now()
#         shapes = table.rows[1].cells[0].part.slide.shapes
#
#         for image in image_dicts:
#
#             left = Inches(image.get('left', self.min_left))
#             top = Inches(image.get('top', self.min_top))
#             width = Inches(image.get('width', self.max_width))
#             height = Inches(image.get('height', self.max_height))
#
#             if image['pic_type'] == 'stream':
#
#                 file_stream = StringIO.StringIO()
#                 file_stream.write(image['pic_stream'])
#                 file_stream.seek(0)
#                 shapes.add_picture(file_stream, left, top, width, height)
#                 file_stream.close()
#
#             else:
#
#                 shapes.add_picture(image['pic_path'], left, top, width, height)
#
#         print datetime.datetime.now()
#
#     def save(self, path_or_stream):
#         self.ppt.save(path_or_stream)