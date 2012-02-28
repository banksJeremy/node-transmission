TRANSMISSION=transmission-2.50

module: $(TRANSMISSION)/libtransmission/libtransmission.a
	node-waf configure
	node-waf build

$(TRANSMISSION)/libtransmission/libtransmission.a: $(TRANSMISSION)/Makefile
	cd "$(TRANSMISSION)" && make

$(TRANSMISSION)/Makefile:
	cd "$(TRANSMISSION)" && ./configure --disable-nls --disable-gtk --disable-mac --enable-cli --enable-daemon

.PHONY: module
