from pox.core import core
from pox.lib.util import str_to_dpid
from pox.forwarding.l2_learning import LearningSwitch


def launch (ignore_dpid):
  ignore_dpid = str_to_dpid(ignore_dpid)

  def _handle_ConnectionUp (event):
    if event.dpid != ignore_dpid:
      core.getLogger().info("Connection %s" % (event.connection,))
      LearningSwitch(event.connection, False)

  core.openflow.addListenerByName("ConnectionUp", _handle_ConnectionUp)