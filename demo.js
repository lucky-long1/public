function(t) {
                    var e, n = new Promise((function(n, r) {
                        e = $.ajax(i(i({}, t), {}, {
                            error: function(t, e, n) {
                                "abort" !== e && r({
                                    jqXHR: t,
                                    textStatus: e,
                                    errorThrown: n
                                })
                            }
                        })).done((function(t) {
                            n({
                                response: t
                            })
                        }
                        ))
                    }
                    )), r = {
                        inst: e,
                        promise: n
                    };
                    return this.translateXhr.push(r),
                    r
                }
            }, {
                key: "startOnce",
                value: (a = u(s().mark((function t() {
                    var e, n, r, o;
                    return s().wrap((function(t) {
                        for (; ; )
                            switch (t.prev = t.next) {
                            case 0:
                                return this.abort(),
                                t.next = 3,
                                this.getAceSign();
                            case 3:
                                return e = t.sent,
                                n = this.paramData.from,
                                r = this.paramData.to,
                                o = this.ajax({
                                    type: "POST",
                                    url: "/v2transapi?from=".concat(encodeURIComponent(n), "&to=").concat(encodeURIComponent(r)),
                                    cache: !1,
                                    data: this.paramData,
                                    headers: {
                                        "Acs-Token": e
                                    }
                                }),
                                t.prev = 7,
                                t.t0 = this,
                                t.next = 11,
                                o.promise;
                            case 11:
                                t.t1 = t.sent.response,
                                t.t2 = {
                                    type: "once",
                                    response: t.t1
                                },
                                t.t0.done.call(t.t0, t.t2),
                                t.next = 20;
                                break;
                            case 16:
                                t.prev = 16,
                                t.t3 = t.catch(7),
                                console.warn(t.t3),
                                this.fail(t.t3);
                            case 20:
                            case "end":
                                return t.stop()
                            }
                    }
                    ), t, this, [[7, 16]])
                }
                )))
