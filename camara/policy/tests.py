# -*- coding: utf-8 -*-
import unittest
from camara.policy.testing import CAMARA_POLICY_INTEGRATION_TESTING

class TestSetup(unittest.TestCase):
	layer = CAMARA_POLICY_INTEGRATION_TESTING

  	def test_portal_title(self):
		portal = self.layer['portal']
		self.assertEqual(
			"Câmara dos Deputados",
			portal.getProperty('title')
			)

	def test_portal_description(self):
		portal = self.layer['portal']
		self.assertEqual(
			"Bem vindo ao Portal da Camara dos Deputados",
			portal.getProperty('description')
			)
 


