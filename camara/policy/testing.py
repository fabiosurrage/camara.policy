from plone.app.testing import PloneSandboxLayer
from plone.app.testing import applyProfile
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import IntegrationTesting
from zope.configuration import xmlconfig


class CamaraPolicy(PloneSandboxLayer):
	defaultBases = (PLONE_FIXTURE,)

	def setUpZope(self, app, configurationContext):
		# Load ZCML
		import camara.policy
		xmlconfig.file('configure.zcml',
			camara.policy,
			context=configurationContext
		)

	def setUpPloneSite(self, portal):
		applyProfile(portal, 'camara.policy:default')

CAMARA_POLICY_FIXTURE = CamaraPolicy()
CAMARA_POLICY_INTEGRATION_TESTING = IntegrationTesting(
	bases=(CAMARA_POLICY_FIXTURE,),
	name="Camara:Integration"
	)

