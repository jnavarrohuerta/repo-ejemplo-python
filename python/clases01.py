class Television(object):
	"""docstring for Television"""
	def __init__(self):
		self.prendida=False
		self.canal=2

tv_cuarto = Television()
tv_sala = Television()
print(tv_cuarto.prendida)
print(tv_cuarto.canal)
tv_sala.canal = 5
print(tv_cuarto.canal)