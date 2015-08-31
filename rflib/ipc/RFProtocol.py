import bson
import pymongo as mongo

from rflib.types.Match import Match
from rflib.types.Action import Action
from rflib.types.Option import Option
from MongoIPC import MongoIPCMessage

format_id = lambda dp_id: hex(dp_id).rstrip('L')

PORT_REGISTER = 0
PORT_CONFIG = 1
DATAPATH_PORT_REGISTER = 2
DATAPATH_DOWN = 3
VIRTUAL_PLANE_MAP = 4
DATA_PLANE_MAP = 5
ROUTE_MOD = 6
SUSPECT_FLOW = 7
IPTABLES_REGISTER = 8
IPTABLES_REGISTER_DYNAMIC = 9

class PortRegister(MongoIPCMessage):
    def __init__(self, vm_id=None, vm_port=None, hwaddress=None):
        self.set_vm_id(vm_id)
        self.set_vm_port(vm_port)
        self.set_hwaddress(hwaddress)

    def get_type(self):
        return PORT_REGISTER

    def get_vm_id(self):
        return self.vm_id

    def set_vm_id(self, vm_id):
        vm_id = 0 if vm_id is None else vm_id
        try:
            self.vm_id = int(vm_id)
        except:
            self.vm_id = 0

    def get_vm_port(self):
        return self.vm_port

    def set_vm_port(self, vm_port):
        vm_port = 0 if vm_port is None else vm_port
        try:
            self.vm_port = int(vm_port)
        except:
            self.vm_port = 0

    def get_hwaddress(self):
        return self.hwaddress

    def set_hwaddress(self, hwaddress):
        hwaddress = "" if hwaddress is None else hwaddress
        try:
            self.hwaddress = str(hwaddress)
        except:
            self.hwaddress = ""

    def from_dict(self, data):
        self.set_vm_id(data["vm_id"])
        self.set_vm_port(data["vm_port"])
        self.set_hwaddress(data["hwaddress"])

    def to_dict(self):
        data = {}
        data["vm_id"] = str(self.get_vm_id())
        data["vm_port"] = str(self.get_vm_port())
        data["hwaddress"] = str(self.get_hwaddress())
        return data

    def from_bson(self, data):
        data = bson.BSON.decode(data)
        self.from_dict(data)

    def to_bson(self):
        return bson.BSON.encode(self.get_dict())

    def __str__(self):
        s = "PortRegister\n"
        s += "  vm_id: " + format_id(self.get_vm_id()) + "\n"
        s += "  vm_port: " + str(self.get_vm_port()) + "\n"
        s += "  hwaddress: " + str(self.get_hwaddress()) + "\n"
        return s

class PortConfig(MongoIPCMessage):
    def __init__(self, vm_id=None, vm_port=None, operation_id=None):
        self.set_vm_id(vm_id)
        self.set_vm_port(vm_port)
        self.set_operation_id(operation_id)

    def get_type(self):
        return PORT_CONFIG

    def get_vm_id(self):
        return self.vm_id

    def set_vm_id(self, vm_id):
        vm_id = 0 if vm_id is None else vm_id
        try:
            self.vm_id = int(vm_id)
        except:
            self.vm_id = 0

    def get_vm_port(self):
        return self.vm_port

    def set_vm_port(self, vm_port):
        vm_port = 0 if vm_port is None else vm_port
        try:
            self.vm_port = int(vm_port)
        except:
            self.vm_port = 0

    def get_operation_id(self):
        return self.operation_id

    def set_operation_id(self, operation_id):
        operation_id = 0 if operation_id is None else operation_id
        try:
            self.operation_id = int(operation_id)
        except:
            self.operation_id = 0

    def from_dict(self, data):
        self.set_vm_id(data["vm_id"])
        self.set_vm_port(data["vm_port"])
        self.set_operation_id(data["operation_id"])

    def to_dict(self):
        data = {}
        data["vm_id"] = str(self.get_vm_id())
        data["vm_port"] = str(self.get_vm_port())
        data["operation_id"] = str(self.get_operation_id())
        return data

    def from_bson(self, data):
        data = bson.BSON.decode(data)
        self.from_dict(data)

    def to_bson(self):
        return bson.BSON.encode(self.get_dict())

    def __str__(self):
        s = "PortConfig\n"
        s += "  vm_id: " + format_id(self.get_vm_id()) + "\n"
        s += "  vm_port: " + str(self.get_vm_port()) + "\n"
        s += "  operation_id: " + str(self.get_operation_id()) + "\n"
        return s

class DatapathPortRegister(MongoIPCMessage):
    def __init__(self, ct_id=None, dp_id=None, dp_port=None):
        self.set_ct_id(ct_id)
        self.set_dp_id(dp_id)
        self.set_dp_port(dp_port)

    def get_type(self):
        return DATAPATH_PORT_REGISTER

    def get_ct_id(self):
        return self.ct_id

    def set_ct_id(self, ct_id):
        ct_id = 0 if ct_id is None else ct_id
        try:
            self.ct_id = int(ct_id)
        except:
            self.ct_id = 0

    def get_dp_id(self):
        return self.dp_id

    def set_dp_id(self, dp_id):
        dp_id = 0 if dp_id is None else dp_id
        try:
            self.dp_id = int(dp_id)
        except:
            self.dp_id = 0

    def get_dp_port(self):
        return self.dp_port

    def set_dp_port(self, dp_port):
        dp_port = 0 if dp_port is None else dp_port
        try:
            self.dp_port = int(dp_port)
        except:
            self.dp_port = 0

    def from_dict(self, data):
        self.set_ct_id(data["ct_id"])
        self.set_dp_id(data["dp_id"])
        self.set_dp_port(data["dp_port"])

    def to_dict(self):
        data = {}
        data["ct_id"] = str(self.get_ct_id())
        data["dp_id"] = str(self.get_dp_id())
        data["dp_port"] = str(self.get_dp_port())
        return data

    def from_bson(self, data):
        data = bson.BSON.decode(data)
        self.from_dict(data)

    def to_bson(self):
        return bson.BSON.encode(self.get_dict())

    def __str__(self):
        s = "DatapathPortRegister\n"
        s += "  ct_id: " + format_id(self.get_ct_id()) + "\n"
        s += "  dp_id: " + format_id(self.get_dp_id()) + "\n"
        s += "  dp_port: " + str(self.get_dp_port()) + "\n"
        return s

class DatapathDown(MongoIPCMessage):
    def __init__(self, ct_id=None, dp_id=None):
        self.set_ct_id(ct_id)
        self.set_dp_id(dp_id)

    def get_type(self):
        return DATAPATH_DOWN

    def get_ct_id(self):
        return self.ct_id

    def set_ct_id(self, ct_id):
        ct_id = 0 if ct_id is None else ct_id
        try:
            self.ct_id = int(ct_id)
        except:
            self.ct_id = 0

    def get_dp_id(self):
        return self.dp_id

    def set_dp_id(self, dp_id):
        dp_id = 0 if dp_id is None else dp_id
        try:
            self.dp_id = int(dp_id)
        except:
            self.dp_id = 0

    def from_dict(self, data):
        self.set_ct_id(data["ct_id"])
        self.set_dp_id(data["dp_id"])

    def to_dict(self):
        data = {}
        data["ct_id"] = str(self.get_ct_id())
        data["dp_id"] = str(self.get_dp_id())
        return data

    def from_bson(self, data):
        data = bson.BSON.decode(data)
        self.from_dict(data)

    def to_bson(self):
        return bson.BSON.encode(self.get_dict())

    def __str__(self):
        s = "DatapathDown\n"
        s += "  ct_id: " + format_id(self.get_ct_id()) + "\n"
        s += "  dp_id: " + format_id(self.get_dp_id()) + "\n"
        return s

class VirtualPlaneMap(MongoIPCMessage):
    def __init__(self, vm_id=None, vm_port=None, vs_id=None, vs_port=None):
        self.set_vm_id(vm_id)
        self.set_vm_port(vm_port)
        self.set_vs_id(vs_id)
        self.set_vs_port(vs_port)

    def get_type(self):
        return VIRTUAL_PLANE_MAP

    def get_vm_id(self):
        return self.vm_id

    def set_vm_id(self, vm_id):
        vm_id = 0 if vm_id is None else vm_id
        try:
            self.vm_id = int(vm_id)
        except:
            self.vm_id = 0

    def get_vm_port(self):
        return self.vm_port

    def set_vm_port(self, vm_port):
        vm_port = 0 if vm_port is None else vm_port
        try:
            self.vm_port = int(vm_port)
        except:
            self.vm_port = 0

    def get_vs_id(self):
        return self.vs_id

    def set_vs_id(self, vs_id):
        vs_id = 0 if vs_id is None else vs_id
        try:
            self.vs_id = int(vs_id)
        except:
            self.vs_id = 0

    def get_vs_port(self):
        return self.vs_port

    def set_vs_port(self, vs_port):
        vs_port = 0 if vs_port is None else vs_port
        try:
            self.vs_port = int(vs_port)
        except:
            self.vs_port = 0

    def from_dict(self, data):
        self.set_vm_id(data["vm_id"])
        self.set_vm_port(data["vm_port"])
        self.set_vs_id(data["vs_id"])
        self.set_vs_port(data["vs_port"])

    def to_dict(self):
        data = {}
        data["vm_id"] = str(self.get_vm_id())
        data["vm_port"] = str(self.get_vm_port())
        data["vs_id"] = str(self.get_vs_id())
        data["vs_port"] = str(self.get_vs_port())
        return data

    def from_bson(self, data):
        data = bson.BSON.decode(data)
        self.from_dict(data)

    def to_bson(self):
        return bson.BSON.encode(self.get_dict())

    def __str__(self):
        s = "VirtualPlaneMap\n"
        s += "  vm_id: " + format_id(self.get_vm_id()) + "\n"
        s += "  vm_port: " + str(self.get_vm_port()) + "\n"
        s += "  vs_id: " + format_id(self.get_vs_id()) + "\n"
        s += "  vs_port: " + str(self.get_vs_port()) + "\n"
        return s

class DataPlaneMap(MongoIPCMessage):
    def __init__(self, ct_id=None, dp_id=None, dp_port=None, vs_id=None, vs_port=None):
        self.set_ct_id(ct_id)
        self.set_dp_id(dp_id)
        self.set_dp_port(dp_port)
        self.set_vs_id(vs_id)
        self.set_vs_port(vs_port)

    def get_type(self):
        return DATA_PLANE_MAP

    def get_ct_id(self):
        return self.ct_id

    def set_ct_id(self, ct_id):
        ct_id = 0 if ct_id is None else ct_id
        try:
            self.ct_id = int(ct_id)
        except:
            self.ct_id = 0

    def get_dp_id(self):
        return self.dp_id

    def set_dp_id(self, dp_id):
        dp_id = 0 if dp_id is None else dp_id
        try:
            self.dp_id = int(dp_id)
        except:
            self.dp_id = 0

    def get_dp_port(self):
        return self.dp_port

    def set_dp_port(self, dp_port):
        dp_port = 0 if dp_port is None else dp_port
        try:
            self.dp_port = int(dp_port)
        except:
            self.dp_port = 0

    def get_vs_id(self):
        return self.vs_id

    def set_vs_id(self, vs_id):
        vs_id = 0 if vs_id is None else vs_id
        try:
            self.vs_id = int(vs_id)
        except:
            self.vs_id = 0

    def get_vs_port(self):
        return self.vs_port

    def set_vs_port(self, vs_port):
        vs_port = 0 if vs_port is None else vs_port
        try:
            self.vs_port = int(vs_port)
        except:
            self.vs_port = 0

    def from_dict(self, data):
        self.set_ct_id(data["ct_id"])
        self.set_dp_id(data["dp_id"])
        self.set_dp_port(data["dp_port"])
        self.set_vs_id(data["vs_id"])
        self.set_vs_port(data["vs_port"])

    def to_dict(self):
        data = {}
        data["ct_id"] = str(self.get_ct_id())
        data["dp_id"] = str(self.get_dp_id())
        data["dp_port"] = str(self.get_dp_port())
        data["vs_id"] = str(self.get_vs_id())
        data["vs_port"] = str(self.get_vs_port())
        return data

    def from_bson(self, data):
        data = bson.BSON.decode(data)
        self.from_dict(data)

    def to_bson(self):
        return bson.BSON.encode(self.get_dict())

    def __str__(self):
        s = "DataPlaneMap\n"
        s += "  ct_id: " + format_id(self.get_ct_id()) + "\n"
        s += "  dp_id: " + format_id(self.get_dp_id()) + "\n"
        s += "  dp_port: " + str(self.get_dp_port()) + "\n"
        s += "  vs_id: " + format_id(self.get_vs_id()) + "\n"
        s += "  vs_port: " + str(self.get_vs_port()) + "\n"
        return s

class RouteMod(MongoIPCMessage):
    def __init__(self, mod=None, id=None, matches=None, actions=None, options=None):
        self.set_mod(mod)
        self.set_id(id)
        self.set_matches(matches)
        self.set_actions(actions)
        self.set_options(options)

    def get_type(self):
        return ROUTE_MOD

    def get_mod(self):
        return self.mod

    def set_mod(self, mod):
        mod = 0 if mod is None else mod
        try:
            self.mod = int(mod)
        except:
            self.mod = 0

    def get_id(self):
        return self.id

    def set_id(self, id):
        id = 0 if id is None else id
        try:
            self.id = int(id)
        except:
            self.id = 0

    def get_matches(self):
        return self.matches

    def set_matches(self, matches):
        matches = list() if matches is None else matches
        try:
            self.matches = list(matches)
        except:
            self.matches = list()

    def add_match(self, match):
        self.matches.append(match.to_dict())

    def get_actions(self):
        return self.actions

    def set_actions(self, actions):
        actions = list() if actions is None else actions
        try:
            self.actions = list(actions)
        except:
            self.actions = list()

    def add_action(self, action):
        self.actions.append(action.to_dict())

    def get_options(self):
        return self.options

    def set_options(self, options):
        options = list() if options is None else options
        try:
            self.options = list(options)
        except:
            self.options = list()

    def add_option(self, option):
        self.options.append(option.to_dict())

    def from_dict(self, data):
        self.set_mod(data["mod"])
        self.set_id(data["id"])
        self.set_matches(data["matches"])
        self.set_actions(data["actions"])
        self.set_options(data["options"])

    def to_dict(self):
        data = {}
        data["mod"] = str(self.get_mod())
        data["id"] = str(self.get_id())
        data["matches"] = self.get_matches()
        data["actions"] = self.get_actions()
        data["options"] = self.get_options()
        return data

    def from_bson(self, data):
        data = bson.BSON.decode(data)
        self.from_dict(data)

    def to_bson(self):
        return bson.BSON.encode(self.get_dict())

    def __str__(self):
        s = "RouteMod\n"
        s += "  mod: " + str(self.get_mod()) + "\n"
        s += "  id: " + format_id(self.get_id()) + "\n"
        s += "  matches:\n"
        for match in self.get_matches():
            s += "    " + str(Match.from_dict(match)) + "\n"
        s += "  actions:\n"
        for action in self.get_actions():
            s += "    " + str(Action.from_dict(action)) + "\n"
        s += "  options:\n"
        for option in self.get_options():
            s += "    " + str(Option.from_dict(option)) + "\n"
        return s

class SuspectFlow(MongoIPCMessage):
    def __init__(self, mod=None, vm_id=None, dp_id=None, vm_port=None, matches=None, ip_src=None, gateway=None):
        self.set_mod(mod)
        self.set_vm_id(vm_id)
        self.set_dp_id(dp_id)
        self.set_vm_port(vm_port)
        self.set_matches(matches)
        self.set_ip_src(ip_src)
        self.set_gateway(gateway)

    def get_type(self):
        return SUSPECT_FLOW

    def get_mod(self):
        return self.mod

    def set_mod(self, mod):
        mod = 0 if mod is None else mod
        try:
            self.mod = int(mod)
        except:
            self.mod = 0

    def get_vm_id(self):
        return self.vm_id

    def set_vm_id(self, vm_id):
        vm_id = 0 if vm_id is None else vm_id
        try:
            self.vm_id = int(vm_id)
        except:
            self.vm_id = 0

    def get_dp_id(self):
        return self.dp_id

    def set_dp_id(self, dp_id):
        dp_id = 0 if dp_id is None else dp_id
        try:
            self.dp_id = int(dp_id)
        except:
            self.dp_id = 0

    def get_vm_port(self):
        return self.vm_port

    def set_vm_port(self, vm_port):
        vm_port = 0 if vm_port is None else vm_port
        try:
            self.vm_port = int(vm_port)
        except:
            self.vm_port = 0

    def get_matches(self):
        return self.matches

    def set_matches(self, matches):
        matches = list() if matches is None else matches
        try:
            self.matches = list(matches)
        except:
            self.matches = list()

    def add_match(self, match):
        self.matches.append(match.to_dict())

    def get_ip_src(self):
        return self.ip_src

    def set_ip_src(self, ip_src):
        ip_src = "" if ip_src is None else ip_src
        try:
            self.ip_src = str(ip_src)
        except:
            self.ip_src = ""

    def get_gateway(self):
        return self.gateway

    def set_gateway(self, gateway):
        gateway = "" if gateway is None else gateway
        try:
            self.gateway = str(gateway)
        except:
            self.gateway = ""

    def from_dict(self, data):
        self.set_mod(data["mod"])
        self.set_vm_id(data["vm_id"])
        self.set_dp_id(data["dp_id"])
        self.set_vm_port(data["vm_port"])
        self.set_matches(data["matches"])
        self.set_ip_src(data["ip_src"])
        self.set_gateway(data["gateway"])

    def to_dict(self):
        data = {}
        data["mod"] = str(self.get_mod())
        data["vm_id"] = str(self.get_vm_id())
        data["dp_id"] = str(self.get_dp_id())
        data["vm_port"] = str(self.get_vm_port())
        data["matches"] = self.get_matches()
        data["ip_src"] = self.get_ip_src()
        data["gateway"] = self.get_gateway()
        return data

    def from_bson(self, data):
        data = bson.BSON.decode(data)
        self.from_dict(data)

    def to_bson(self):
        return bson.BSON.encode(self.get_dict())

    def __str__(self):
        s = "SuspectFlow\n"
        s += "  mod: " + str(self.get_mod()) + "\n"
        s += "  vm_id: " + format_id(self.get_vm_id()) + "\n"
        s += "  dp_id: " + format_id(self.get_dp_id()) + "\n"
        s += "  vm_port: " + str(self.get_vm_port()) + "\n"
        s += "  matches:\n"
        for match in self.get_matches():
            s += "    " + str(Match.from_dict(match)) + "\n"
        s += "  ip_src: " + str(self.get_ip_src()) + "\n"
        s += "  gateway: " + str(self.get_gateway()) + "\n"
        return s

class IptablesRegister(MongoIPCMessage):
    def __init__(self, vm_id=None, vm_port=None, hwaddress=None, blocked_ip=None):
        self.set_vm_id(vm_id)
        self.set_vm_port(vm_port)
        self.set_hwaddress(hwaddress)
        self.set_blocked_ip(blocked_ip)

    def get_type(self):
        return IPTABLES_REGISTER

    def get_vm_id(self):
        return self.vm_id

    def set_vm_id(self, vm_id):
        vm_id = 0 if vm_id is None else vm_id
        try:
            self.vm_id = int(vm_id)
        except:
            self.vm_id = 0

    def get_vm_port(self):
        return self.vm_port

    def set_vm_port(self, vm_port):
        vm_port = 0 if vm_port is None else vm_port
        try:
            self.vm_port = int(vm_port)
        except:
            self.vm_port = 0

    def get_hwaddress(self):
        return self.hwaddress

    def set_hwaddress(self, hwaddress):
        hwaddress = "" if hwaddress is None else hwaddress
        try:
            self.hwaddress = str(hwaddress)
        except:
            self.hwaddress = ""

    def get_blocked_ip(self):
        return self.blocked_ip

    def set_blocked_ip(self, blocked_ip):
        blocked_ip = "" if blocked_ip is None else blocked_ip
        try:
            self.blocked_ip = str(blocked_ip)
        except:
            self.blocked_ip = ""

    def from_dict(self, data):
        self.set_vm_id(data["vm_id"])
        self.set_vm_port(data["vm_port"])
        self.set_hwaddress(data["hwaddress"])
        self.set_blocked_ip(data["blocked_ip"])

    def to_dict(self):
        data = {}
        data["vm_id"] = str(self.get_vm_id())
        data["vm_port"] = str(self.get_vm_port())
        data["hwaddress"] = str(self.get_hwaddress())
        data["blocked_ip"] = self.get_blocked_ip()
        return data

    def from_bson(self, data):
        data = bson.BSON.decode(data)
        self.from_dict(data)

    def to_bson(self):
        return bson.BSON.encode(self.get_dict())

    def __str__(self):
        s = "IptablesRegister\n"
        s += "  vm_id: " + format_id(self.get_vm_id()) + "\n"
        s += "  vm_port: " + str(self.get_vm_port()) + "\n"
        s += "  hwaddress: " + str(self.get_hwaddress()) + "\n"
        s += "  blocked_ip: " + str(self.get_blocked_ip()) + "\n"
        return s

class IptablesRegisterDynamic(MongoIPCMessage):
    def __init__(self, vm_id=None, vm_port=None, blocked_ip=None):
        self.set_vm_id(vm_id)
        self.set_vm_port(vm_port)
        self.set_blocked_ip(blocked_ip)

    def get_type(self):
        return IPTABLES_REGISTER_DYNAMIC

    def get_vm_id(self):
        return self.vm_id

    def set_vm_id(self, vm_id):
        vm_id = 0 if vm_id is None else vm_id
        try:
            self.vm_id = int(vm_id)
        except:
            self.vm_id = 0

    def get_vm_port(self):
        return self.vm_port

    def set_vm_port(self, vm_port):
        vm_port = 0 if vm_port is None else vm_port
        try:
            self.vm_port = int(vm_port)
        except:
            self.vm_port = 0

    def get_blocked_ip(self):
        return self.blocked_ip

    def set_blocked_ip(self, blocked_ip):
        blocked_ip = "" if blocked_ip is None else blocked_ip
        try:
            self.blocked_ip = str(blocked_ip)
        except:
            self.blocked_ip = ""

    def from_dict(self, data):
        self.set_vm_id(data["vm_id"])
        self.set_vm_port(data["vm_port"])
        self.set_blocked_ip(data["blocked_ip"])

    def to_dict(self):
        data = {}
        data["vm_id"] = str(self.get_vm_id())
        data["vm_port"] = str(self.get_vm_port())
        data["blocked_ip"] = self.get_blocked_ip()
        return data

    def from_bson(self, data):
        data = bson.BSON.decode(data)
        self.from_dict(data)

    def to_bson(self):
        return bson.BSON.encode(self.get_dict())

    def __str__(self):
        s = "IptablesRegisterDynamic\n"
        s += "  vm_id: " + format_id(self.get_vm_id()) + "\n"
        s += "  vm_port: " + str(self.get_vm_port()) + "\n"
        s += "  blocked_ip: " + str(self.get_blocked_ip()) + "\n"
        return s
