# Copyright (C) 2014 Google Inc., authors, and contributors <see AUTHORS file>
# Licensed under http://www.apache.org/licenses/LICENSE-2.0 <see LICENSE file>
# Created By: silas@reciprocitylabs.com
# Maintained By: silas@reciprocitylabs.com


from ggrc.models.all_models import register_model

from .risk import Risk
from .risk_object import RiskObject
from .threat_actor import ThreatActor

register_model(Risk)
register_model(RiskObject)
register_model(ThreatActor)
