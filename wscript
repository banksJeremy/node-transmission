def set_options(ctx):
    ctx.tool_options('compiler_cxx')

def configure(ctx):
    ctx.check_tool('compiler_cxx')
    ctx.check_tool('node_addon')

def build(ctx):
    t = ctx.new_task_gen('cxx', 'shlib', 'node_addon')
    ctx.env.append_value('LINKFLAGS', '../transmission-2.50/libtransmission/libtransmission.a')
    ctx.env.append_value('LINKFLAGS', '../transmission-2.50/third-party/dht/libdht.a')
    ctx.env.append_value('LINKFLAGS', '../transmission-2.50/third-party/libnatpmp/libnatpmp.a')
    ctx.env.append_value('LINKFLAGS', '../transmission-2.50/third-party/libutp/libutp.a')
    ctx.env.append_value('LINKFLAGS', '../transmission-2.50/third-party/miniupnp/libminiupnp.a')
    ctx.env.append_value('LINKFLAGS', "-levent")
    ctx.env.append_value('LINKFLAGS', "-lcurl")
    ctx.env.append_value('LINKFLAGS', "-lz")
    t.source = ctx.path.ant_glob("*.cpp")
    t.target = 'transmission'
