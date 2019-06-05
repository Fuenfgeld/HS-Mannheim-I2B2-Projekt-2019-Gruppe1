setTimeout(whole_func, 2000);

function whole_func() {
    // alert('jstree loaded')
    /*! jsTree - v3.0.9 - 2015-01-05 - (MIT) */
    !function (a) {
        "use strict";
        "function" == typeof define && define.amd ? define(["frontend/app/assets/jquery"], a) : a("object" == typeof exports ? require("frontend/app/assets/jquery") : jQuery)
    }(function (a, b) {
        "use strict";
        if (!a.jstree) {
            var c = 0, d = !1, e = !1, f = !1, g = [], h = a("script:last").attr("src"), i = document,
                j = i.createElement("LI"), k, l;
            j.setAttribute("role", "treeitem"), k = i.createElement("I"), k.className = "jstree-icon jstree-ocl", k.setAttribute("role", "presentation"), j.appendChild(k), k = i.createElement("A"), k.className = "jstree-anchor", k.setAttribute("href", "#"), k.setAttribute("tabindex", "-1"), l = i.createElement("I"), l.className = "jstree-icon jstree-themeicon", l.setAttribute("role", "presentation"), k.appendChild(l), j.appendChild(k), k = l = null, a.jstree = {
                version: "3.0.9",
                defaults: {plugins: []},
                plugins: {},
                path: h && -1 !== h.indexOf("/") ? h.replace(/\/[^\/]+$/, "") : "",
                idregex: /[\\:&!^|()\[\]<>@*'+~#";.,=\- \/${}%?`]/g
            }, a.jstree.create = function (b, d) {
                var e = new a.jstree.core(++c), f = d;
                return d = a.extend(!0, {}, a.jstree.defaults, d), f && f.plugins && (d.plugins = f.plugins), a.each(d.plugins, function (a, b) {
                    "core" !== a && (e = e.plugin(b, d[b]))
                }), e.init(b, d), e
            }, a.jstree.destroy = function () {
                a(".jstree:jstree").jstree("destroy"), a(document).off(".jstree")
            }, a.jstree.core = function (a) {
                this._id = a, this._cnt = 0, this._wrk = null, this._data = {
                    core: {
                        themes: {
                            name: !1,
                            dots: !1,
                            icons: !1
                        }, selected: [], last_error: {}, working: !1, worker_queue: [], focused: null
                    }
                }
            }, a.jstree.reference = function (b) {
                var c = null, d = null;
                if (b && b.id && (b = b.id), !d || !d.length) try {
                    d = a(b)
                } catch (e) {
                }
                if (!d || !d.length) try {
                    d = a("#" + b.replace(a.jstree.idregex, "\\$&"))
                } catch (e) {
                }
                return d && d.length && (d = d.closest(".jstree")).length && (d = d.data("jstree")) ? c = d : a(".jstree").each(function () {
                    var d = a(this).data("jstree");
                    return d && d._model.data[b] ? (c = d, !1) : void 0
                }), c
            }, a.fn.jstree = function (c) {
                var d = "string" == typeof c, e = Array.prototype.slice.call(arguments, 1), f = null;
                return c !== !0 || this.length ? (this.each(function () {
                    var g = a.jstree.reference(this), h = d && g ? g[c] : null;
                    return f = d && h ? h.apply(g, e) : null, g || d || c !== b && !a.isPlainObject(c) || a(this).data("jstree", new a.jstree.create(this, c)), (g && !d || c === !0) && (f = g || !1), null !== f && f !== b ? !1 : void 0
                }), null !== f && f !== b ? f : this) : !1
            }, a.expr[":"].jstree = a.expr.createPseudo(function (c) {
                return function (c) {
                    return a(c).hasClass("jstree") && a(c).data("jstree") !== b
                }
            }), a.jstree.defaults.core = {
                data: !1,
                strings: !1,
                check_callback: !1,
                error: a.noop,
                animation: 200,
                multiple: !0,
                themes: {name: !1, url: !1, dir: !1, dots: !0, icons: !0, stripes: !1, variant: !1, responsive: !1},
                expand_selected_onload: !0,
                worker: !0,
                force_text: !1,
                dblclick_toggle: !0
            }, a.jstree.core.prototype = {
                plugin: function (b, c) {
                    var d = a.jstree.plugins[b];
                    return d ? (this._data[b] = {}, d.prototype = this, new d(c, this)) : this
                }, init: function (b, c) {
                    this._model = {
                        data: {
                            "#": {
                                id: "#",
                                parent: null,
                                parents: [],
                                children: [],
                                children_d: [],
                                state: {loaded: !1}
                            }
                        },
                        changed: [],
                        force_full_redraw: !1,
                        redraw_timeout: !1,
                        default_state: {loaded: !0, opened: !1, selected: !1, disabled: !1}
                    }, this.element = a(b).addClass("jstree jstree-" + this._id), this.settings = c, this._data.core.ready = !1, this._data.core.loaded = !1, this._data.core.rtl = "rtl" === this.element.css("direction"), this.element[this._data.core.rtl ? "addClass" : "removeClass"]("jstree-rtl"), this.element.attr("role", "tree"), this.settings.core.multiple && this.element.attr("aria-multiselectable", !0), this.element.attr("tabindex") || this.element.attr("tabindex", "0"), this.bind(), this.trigger("init"), this._data.core.original_container_html = this.element.find(" > ul > li").clone(!0), this._data.core.original_container_html.find("li").addBack().contents().filter(function () {
                        return 3 === this.nodeType && (!this.nodeValue || /^\s+$/.test(this.nodeValue))
                    }).remove(), this.element.html("<ul class='jstree-container-ul jstree-children' role='group'><li id='j" + this._id + "_loading' class='jstree-initial-node jstree-loading jstree-leaf jstree-last' role='tree-item'><i class='jstree-icon jstree-ocl'></i><a class='jstree-anchor' href='#'><i class='jstree-icon jstree-themeicon-hidden'></i>" + this.get_string("Loading ...") + "</a></li></ul>"), this.element.attr("aria-activedescendant", "j" + this._id + "_loading"), this._data.core.li_height = this.get_container_ul().children("li").first().height() || 24, this.trigger("loading"), this.load_node("#")
                }, destroy: function (a) {
                    if (this._wrk) try {
                        window.URL.revokeObjectURL(this._wrk), this._wrk = null
                    } catch (b) {
                    }
                    a || this.element.empty(), this.teardown()
                }, teardown: function () {
                    this.unbind(), this.element.removeClass("jstree").removeData("jstree").find("[class^='jstree']").addBack().attr("class", function () {
                        return this.className.replace(/jstree[^ ]*|$/gi, "")
                    }), this.element = null
                }, bind: function () {
                    var b = "", c = null, d = 0;
                    this.element.on("dblclick.jstree", function () {
                        if (document.selection && document.selection.empty) document.selection.empty(); else if (window.getSelection) {
                            var a = window.getSelection();
                            try {
                                a.removeAllRanges(), a.collapse()
                            } catch (b) {
                            }
                        }
                    }).on("mousedown.jstree", a.proxy(function (a) {
                        a.target === this.element[0] && (a.preventDefault(), d = +new Date)
                    }, this)).on("mousedown.jstree", ".jstree-ocl", function (a) {
                        a.preventDefault()
                    }).on("click.jstree", ".jstree-ocl", a.proxy(function (a) {
                        this.toggle_node(a.target)
                    }, this)).on("dblclick.jstree", ".jstree-anchor", a.proxy(function (a) {
                        this.settings.core.dblclick_toggle && this.toggle_node(a.target)
                    }, this)).on("click.jstree", ".jstree-anchor", a.proxy(function (b) {
                        b.preventDefault(), b.currentTarget !== document.activeElement && a(b.currentTarget).focus(), this.activate_node(b.currentTarget, b)
                    }, this)).on("keydown.jstree", ".jstree-anchor", a.proxy(function (b) {
                        if ("INPUT" === b.target.tagName) return !0;
                        var c = null;
                        switch (this._data.core.rtl && (37 === b.which ? b.which = 39 : 39 === b.which && (b.which = 37)), b.which) {
                            case 32:
                                b.ctrlKey && (b.type = "click", a(b.currentTarget).trigger(b));
                                break;
                            case 13:
                                b.type = "click", a(b.currentTarget).trigger(b);
                                break;
                            case 37:
                                b.preventDefault(), this.is_open(b.currentTarget) ? this.close_node(b.currentTarget) : (c = this.get_parent(b.currentTarget), c && "#" !== c.id && this.get_node(c, !0).children(".jstree-anchor").focus());
                                break;
                            case 38:
                                b.preventDefault(), c = this.get_prev_dom(b.currentTarget), c && c.length && c.children(".jstree-anchor").focus();
                                break;
                            case 39:
                                b.preventDefault(), this.is_closed(b.currentTarget) ? this.open_node(b.currentTarget, function (a) {
                                    this.get_node(a, !0).children(".jstree-anchor").focus()
                                }) : this.is_open(b.currentTarget) && (c = this.get_node(b.currentTarget, !0).children(".jstree-children")[0], c && a(this._firstChild(c)).children(".jstree-anchor").focus());
                                break;
                            case 40:
                                b.preventDefault(), c = this.get_next_dom(b.currentTarget), c && c.length && c.children(".jstree-anchor").focus();
                                break;
                            case 106:
                                this.open_all();
                                break;
                            case 36:
                                b.preventDefault(), c = this._firstChild(this.get_container_ul()[0]), c && a(c).children(".jstree-anchor").filter(":visible").focus();
                                break;
                            case 35:
                                b.preventDefault(), this.element.find(".jstree-anchor").filter(":visible").last().focus()
                        }
                    }, this)).on("load_node.jstree", a.proxy(function (b, c) {
                        c.status && ("#" !== c.node.id || this._data.core.loaded || (this._data.core.loaded = !0, this._firstChild(this.get_container_ul()[0]) && this.element.attr("aria-activedescendant", this._firstChild(this.get_container_ul()[0]).id), this.trigger("loaded")), this._data.core.ready || setTimeout(a.proxy(function () {
                            if (!this.get_container_ul().find(".jstree-loading").length) {
                                if (this._data.core.ready = !0, this._data.core.selected.length) {
                                    if (this.settings.core.expand_selected_onload) {
                                        var b = [], c, d;
                                        for (c = 0, d = this._data.core.selected.length; d > c; c++) b = b.concat(this._model.data[this._data.core.selected[c]].parents);
                                        for (b = a.vakata.array_unique(b), c = 0, d = b.length; d > c; c++) this.open_node(b[c], !1, 0)
                                    }
                                    this.trigger("changed", {action: "ready", selected: this._data.core.selected})
                                }
                                this.trigger("ready")
                            }
                        }, this), 0))
                    }, this)).on("keypress.jstree", a.proxy(function (d) {
                        if ("INPUT" === d.target.tagName) return !0;
                        c && clearTimeout(c), c = setTimeout(function () {
                            b = ""
                        }, 500);
                        var e = String.fromCharCode(d.which).toLowerCase(),
                            f = this.element.find(".jstree-anchor").filter(":visible"),
                            g = f.index(document.activeElement) || 0, h = !1;
                        if (b += e, b.length > 1) {
                            if (f.slice(g).each(a.proxy(function (c, d) {
                                return 0 === a(d).text().toLowerCase().indexOf(b) ? (a(d).focus(), h = !0, !1) : void 0
                            }, this)), h) return;
                            if (f.slice(0, g).each(a.proxy(function (c, d) {
                                return 0 === a(d).text().toLowerCase().indexOf(b) ? (a(d).focus(), h = !0, !1) : void 0
                            }, this)), h) return
                        }
                        if (new RegExp("^" + e + "+$").test(b)) {
                            if (f.slice(g + 1).each(a.proxy(function (b, c) {
                                return a(c).text().toLowerCase().charAt(0) === e ? (a(c).focus(), h = !0, !1) : void 0
                            }, this)), h) return;
                            if (f.slice(0, g + 1).each(a.proxy(function (b, c) {
                                return a(c).text().toLowerCase().charAt(0) === e ? (a(c).focus(), h = !0, !1) : void 0
                            }, this)), h) return
                        }
                    }, this)).on("init.jstree", a.proxy(function () {
                        var a = this.settings.core.themes;
                        this._data.core.themes.dots = a.dots, this._data.core.themes.stripes = a.stripes, this._data.core.themes.icons = a.icons, this.set_theme(a.name || "default", a.url), this.set_theme_variant(a.variant)
                    }, this)).on("loading.jstree", a.proxy(function () {
                        this[this._data.core.themes.dots ? "show_dots" : "hide_dots"](), this[this._data.core.themes.icons ? "show_icons" : "hide_icons"](), this[this._data.core.themes.stripes ? "show_stripes" : "hide_stripes"]()
                    }, this)).on("blur.jstree", ".jstree-anchor", a.proxy(function (b) {
                        this._data.core.focused = null, a(b.currentTarget).filter(".jstree-hovered").mouseleave(), this.element.attr("tabindex", "0")
                    }, this)).on("focus.jstree", ".jstree-anchor", a.proxy(function (b) {
                        var c = this.get_node(b.currentTarget);
                        c && c.id && (this._data.core.focused = c.id), this.element.find(".jstree-hovered").not(b.currentTarget).mouseleave(), a(b.currentTarget).mouseenter(), this.element.attr("tabindex", "-1")
                    }, this)).on("focus.jstree", a.proxy(function () {
                        +new Date - d > 500 && !this._data.core.focused && (d = 0, this.get_node(this.element.attr("aria-activedescendant"), !0).find("> .jstree-anchor").focus())
                    }, this)).on("mouseenter.jstree", ".jstree-anchor", a.proxy(function (a) {
                        this.hover_node(a.currentTarget)
                    }, this)).on("mouseleave.jstree", ".jstree-anchor", a.proxy(function (a) {
                        this.dehover_node(a.currentTarget)
                    }, this))
                }, unbind: function () {
                    this.element.off(".jstree"), a(document).off(".jstree-" + this._id)
                }, trigger: function (a, b) {
                    b || (b = {}), b.instance = this, this.element.triggerHandler(a.replace(".jstree", "") + ".jstree", b)
                }, get_container: function () {
                    return this.element
                }, get_container_ul: function () {
                    return this.element.children(".jstree-children").first()
                }, get_string: function (b) {
                    var c = this.settings.core.strings;
                    return a.isFunction(c) ? c.call(this, b) : c && c[b] ? c[b] : b
                }, _firstChild: function (a) {
                    a = a ? a.firstChild : null;
                    while (null !== a && 1 !== a.nodeType) a = a.nextSibling;
                    return a
                }, _nextSibling: function (a) {
                    a = a ? a.nextSibling : null;
                    while (null !== a && 1 !== a.nodeType) a = a.nextSibling;
                    return a
                }, _previousSibling: function (a) {
                    a = a ? a.previousSibling : null;
                    while (null !== a && 1 !== a.nodeType) a = a.previousSibling;
                    return a
                }, get_node: function (b, c) {
                    b && b.id && (b = b.id);
                    var d;
                    try {
                        if (this._model.data[b]) b = this._model.data[b]; else if ("string" == typeof b && this._model.data[b.replace(/^#/, "")]) b = this._model.data[b.replace(/^#/, "")]; else if ("string" == typeof b && (d = a("#" + b.replace(a.jstree.idregex, "\\$&"), this.element)).length && this._model.data[d.closest(".jstree-node").attr("id")]) b = this._model.data[d.closest(".jstree-node").attr("id")]; else if ((d = a(b, this.element)).length && this._model.data[d.closest(".jstree-node").attr("id")]) b = this._model.data[d.closest(".jstree-node").attr("id")]; else {
                            if (!(d = a(b, this.element)).length || !d.hasClass("jstree")) return !1;
                            b = this._model.data["#"]
                        }
                        return c && (b = "#" === b.id ? this.element : a("#" + b.id.replace(a.jstree.idregex, "\\$&"), this.element)), b
                    } catch (e) {
                        return !1
                    }
                }, get_path: function (a, b, c) {
                    if (a = a.parents ? a : this.get_node(a), !a || "#" === a.id || !a.parents) return !1;
                    var d, e, f = [];
                    for (f.push(c ? a.id : a.text), d = 0, e = a.parents.length; e > d; d++) f.push(c ? a.parents[d] : this.get_text(a.parents[d]));
                    return f = f.reverse().slice(1), b ? f.join(b) : f
                }, get_next_dom: function (b, c) {
                    var d;
                    if (b = this.get_node(b, !0), b[0] === this.element[0]) {
                        d = this._firstChild(this.get_container_ul()[0]);
                        while (d && 0 === d.offsetHeight) d = this._nextSibling(d);
                        return d ? a(d) : !1
                    }
                    if (!b || !b.length) return !1;
                    if (c) {
                        d = b[0];
                        do d = this._nextSibling(d); while (d && 0 === d.offsetHeight);
                        return d ? a(d) : !1
                    }
                    if (b.hasClass("jstree-open")) {
                        d = this._firstChild(b.children(".jstree-children")[0]);
                        while (d && 0 === d.offsetHeight) d = this._nextSibling(d);
                        if (null !== d) return a(d)
                    }
                    d = b[0];
                    do d = this._nextSibling(d); while (d && 0 === d.offsetHeight);
                    return null !== d ? a(d) : b.parentsUntil(".jstree", ".jstree-node").next(".jstree-node:visible").first()
                }, get_prev_dom: function (b, c) {
                    var d;
                    if (b = this.get_node(b, !0), b[0] === this.element[0]) {
                        d = this.get_container_ul()[0].lastChild;
                        while (d && 0 === d.offsetHeight) d = this._previousSibling(d);
                        return d ? a(d) : !1
                    }
                    if (!b || !b.length) return !1;
                    if (c) {
                        d = b[0];
                        do d = this._previousSibling(d); while (d && 0 === d.offsetHeight);
                        return d ? a(d) : !1
                    }
                    d = b[0];
                    do d = this._previousSibling(d); while (d && 0 === d.offsetHeight);
                    if (null !== d) {
                        b = a(d);
                        while (b.hasClass("jstree-open")) b = b.children(".jstree-children").first().children(".jstree-node:visible:last");
                        return b
                    }
                    return d = b[0].parentNode.parentNode, d && d.className && -1 !== d.className.indexOf("jstree-node") ? a(d) : !1
                }, get_parent: function (a) {
                    return a = this.get_node(a), a && "#" !== a.id ? a.parent : !1
                }, get_children_dom: function (a) {
                    return a = this.get_node(a, !0), a[0] === this.element[0] ? this.get_container_ul().children(".jstree-node") : a && a.length ? a.children(".jstree-children").children(".jstree-node") : !1
                }, is_parent: function (a) {
                    return a = this.get_node(a), a && (a.state.loaded === !1 || a.children.length > 0)
                }, is_loaded: function (a) {
                    return a = this.get_node(a), a && a.state.loaded
                }, is_loading: function (a) {
                    return a = this.get_node(a), a && a.state && a.state.loading
                }, is_open: function (a) {
                    return a = this.get_node(a), a && a.state.opened
                }, is_closed: function (a) {
                    return a = this.get_node(a), a && this.is_parent(a) && !a.state.opened
                }, is_leaf: function (a) {
                    return !this.is_parent(a)
                }, load_node: function (b, c) {
                    var d, e, f, g, h;
                    if (a.isArray(b)) return this._load_nodes(b.slice(), c), !0;
                    if (b = this.get_node(b), !b) return c && c.call(this, b, !1), !1;
                    if (b.state.loaded) {
                        for (b.state.loaded = !1, d = 0, e = b.children_d.length; e > d; d++) {
                            for (f = 0, g = b.parents.length; g > f; f++) this._model.data[b.parents[f]].children_d = a.vakata.array_remove_item(this._model.data[b.parents[f]].children_d, b.children_d[d]);
                            this._model.data[b.children_d[d]].state.selected && (h = !0, this._data.core.selected = a.vakata.array_remove_item(this._data.core.selected, b.children_d[d])), delete this._model.data[b.children_d[d]]
                        }
                        b.children = [], b.children_d = [], h && this.trigger("changed", {
                            action: "load_node",
                            node: b,
                            selected: this._data.core.selected
                        })
                    }
                    return b.state.loading = !0, this.get_node(b, !0).addClass("jstree-loading").attr("aria-busy", !0), this._load_node(b, a.proxy(function (a) {
                        b = this._model.data[b.id], b.state.loading = !1, b.state.loaded = a;
                        var d = this.get_node(b, !0);
                        b.state.loaded && !b.children.length && d && d.length && !d.hasClass("jstree-leaf") && d.removeClass("jstree-closed jstree-open").addClass("jstree-leaf"), d.removeClass("jstree-loading").attr("aria-busy", !1), this.trigger("load_node", {
                            node: b,
                            status: a
                        }), c && c.call(this, b, a)
                    }, this)), !0
                }, _load_nodes: function (a, b, c) {
                    var d = !0, e = function () {
                        this._load_nodes(a, b, !0)
                    }, f = this._model.data, g, h;
                    for (g = 0, h = a.length; h > g; g++) !f[a[g]] || f[a[g]].state.loaded && c || (this.is_loading(a[g]) || this.load_node(a[g], e), d = !1);
                    d && b && !b.done && (b.call(this, a), b.done = !0)
                }, load_all: function (a, b) {
                    if (a || (a = "#"), a = this.get_node(a), !a) return !1;
                    var c = [], d = this._model.data, e = d[a.id].children_d, f, g;
                    for (a.state && !a.state.loaded && c.push(a.id), f = 0, g = e.length; g > f; f++) d[e[f]] && d[e[f]].state && !d[e[f]].state.loaded && c.push(e[f]);
                    c.length ? this._load_nodes(c, function () {
                        this.load_all(a, b)
                    }) : (b && b.call(this, a), this.trigger("load_all", {node: a}))
                }, _load_node: function (b, c) {
                    var d = this.settings.core.data, e;
                    return d ? a.isFunction(d) ? d.call(this, b, a.proxy(function (d) {
                        d === !1 && c.call(this, !1), this["string" == typeof d ? "_append_html_data" : "_append_json_data"](b, "string" == typeof d ? a(d) : d, function (a) {
                            c.call(this, a)
                        })
                    }, this)) : "object" == typeof d ? d.url ? (d = a.extend(!0, {}, d), a.isFunction(d.url) && (d.url = d.url.call(this, b)), a.isFunction(d.data) && (d.data = d.data.call(this, b)), a.ajax(d).done(a.proxy(function (d, e, f) {
                        var g = f.getResponseHeader("Content-Type");
                        return -1 !== g.indexOf("json") || "object" == typeof d ? this._append_json_data(b, d, function (a) {
                            c.call(this, a)
                        }) : -1 !== g.indexOf("html") || "string" == typeof d ? this._append_html_data(b, a(d), function (a) {
                            c.call(this, a)
                        }) : (this._data.core.last_error = {
                            error: "ajax",
                            plugin: "core",
                            id: "core_04",
                            reason: "Could not load node",
                            data: JSON.stringify({id: b.id, xhr: f})
                        }, this.settings.core.error.call(this, this._data.core.last_error), c.call(this, !1))
                    }, this)).fail(a.proxy(function (a) {
                        c.call(this, !1), this._data.core.last_error = {
                            error: "ajax",
                            plugin: "core",
                            id: "core_04",
                            reason: "Could not load node",
                            data: JSON.stringify({id: b.id, xhr: a})
                        }, this.settings.core.error.call(this, this._data.core.last_error)
                    }, this))) : (e = a.isArray(d) || a.isPlainObject(d) ? JSON.parse(JSON.stringify(d)) : d, "#" === b.id ? this._append_json_data(b, e, function (a) {
                        c.call(this, a)
                    }) : (this._data.core.last_error = {
                        error: "nodata",
                        plugin: "core",
                        id: "core_05",
                        reason: "Could not load node",
                        data: JSON.stringify({id: b.id})
                    }, this.settings.core.error.call(this, this._data.core.last_error), c.call(this, !1))) : "string" == typeof d ? "#" === b.id ? this._append_html_data(b, a(d), function (a) {
                        c.call(this, a)
                    }) : (this._data.core.last_error = {
                        error: "nodata",
                        plugin: "core",
                        id: "core_06",
                        reason: "Could not load node",
                        data: JSON.stringify({id: b.id})
                    }, this.settings.core.error.call(this, this._data.core.last_error), c.call(this, !1)) : c.call(this, !1) : "#" === b.id ? this._append_html_data(b, this._data.core.original_container_html.clone(!0), function (a) {
                        c.call(this, a)
                    }) : c.call(this, !1)
                }, _node_changed: function (a) {
                    a = this.get_node(a), a && this._model.changed.push(a.id)
                }, _append_html_data: function (b, c, d) {
                    b = this.get_node(b), b.children = [], b.children_d = [];
                    var e = c.is("ul") ? c.children() : c, f = b.id, g = [], h = [], i = this._model.data, j = i[f],
                        k = this._data.core.selected.length, l, m, n;
                    for (e.each(a.proxy(function (b, c) {
                        l = this._parse_model_from_html(a(c), f, j.parents.concat()), l && (g.push(l), h.push(l), i[l].children_d.length && (h = h.concat(i[l].children_d)))
                    }, this)), j.children = g, j.children_d = h, m = 0, n = j.parents.length; n > m; m++) i[j.parents[m]].children_d = i[j.parents[m]].children_d.concat(h);
                    this.trigger("model", {
                        nodes: h,
                        parent: f
                    }), "#" !== f ? (this._node_changed(f), this.redraw()) : (this.get_container_ul().children(".jstree-initial-node").remove(), this.redraw(!0)), this._data.core.selected.length !== k && this.trigger("changed", {
                        action: "model",
                        selected: this._data.core.selected
                    }), d.call(this, !0)
                }, _append_json_data: function (b, c, d, e) {
                    b = this.get_node(b), b.children = [], b.children_d = [], c.d && (c = c.d, "string" == typeof c && (c = JSON.parse(c))), a.isArray(c) || (c = [c]);
                    var f = null, g = {
                        df: this._model.default_state,
                        dat: c,
                        par: b.id,
                        m: this._model.data,
                        t_id: this._id,
                        t_cnt: this._cnt,
                        sel: this._data.core.selected
                    }, h = function (a, b) {
                        a.data && (a = a.data);
                        var c = a.dat, d = a.par, e = [], f = [], g = [], h = a.df, i = a.t_id, j = a.t_cnt, k = a.m,
                            l = k[d], m = a.sel, n, o, p, q, r = function (a, c, d) {
                                d = d ? d.concat() : [], c && d.unshift(c);
                                var e = a.id.toString(), f, i, j, l, m = {
                                    id: e,
                                    text: a.text || "",
                                    icon: a.icon !== b ? a.icon : !0,
                                    parent: c,
                                    parents: d,
                                    children: a.children || [],
                                    children_d: a.children_d || [],
                                    data: a.data,
                                    state: {},
                                    li_attr: {id: !1},
                                    a_attr: {href: "#"},
                                    original: !1
                                };
                                for (f in h) h.hasOwnProperty(f) && (m.state[f] = h[f]);
                                if (a && a.data && a.data.jstree && a.data.jstree.icon && (m.icon = a.data.jstree.icon), a && a.data && (m.data = a.data, a.data.jstree)) for (f in a.data.jstree) a.data.jstree.hasOwnProperty(f) && (m.state[f] = a.data.jstree[f]);
                                if (a && "object" == typeof a.state) for (f in a.state) a.state.hasOwnProperty(f) && (m.state[f] = a.state[f]);
                                if (a && "object" == typeof a.li_attr) for (f in a.li_attr) a.li_attr.hasOwnProperty(f) && (m.li_attr[f] = a.li_attr[f]);
                                if (m.li_attr.id || (m.li_attr.id = e), a && "object" == typeof a.a_attr) for (f in a.a_attr) a.a_attr.hasOwnProperty(f) && (m.a_attr[f] = a.a_attr[f]);
                                for (a && a.children && a.children === !0 && (m.state.loaded = !1, m.children = [], m.children_d = []), k[m.id] = m, f = 0, i = m.children.length; i > f; f++) j = r(k[m.children[f]], m.id, d), l = k[j], m.children_d.push(j), l.children_d.length && (m.children_d = m.children_d.concat(l.children_d));
                                return delete a.data, delete a.children, k[m.id].original = a, m.state.selected && g.push(m.id), m.id
                            }, s = function (a, c, d) {
                                d = d ? d.concat() : [], c && d.unshift(c);
                                var e = !1, f, l, m, n, o;
                                do e = "j" + i + "_" + ++j; while (k[e]);
                                o = {
                                    id: !1,
                                    text: "string" == typeof a ? a : "",
                                    icon: "object" == typeof a && a.icon !== b ? a.icon : !0,
                                    parent: c,
                                    parents: d,
                                    children: [],
                                    children_d: [],
                                    data: null,
                                    state: {},
                                    li_attr: {id: !1},
                                    a_attr: {href: "#"},
                                    original: !1
                                };
                                for (f in h) h.hasOwnProperty(f) && (o.state[f] = h[f]);
                                if (a && a.id && (o.id = a.id.toString()), a && a.text && (o.text = a.text), a && a.data && a.data.jstree && a.data.jstree.icon && (o.icon = a.data.jstree.icon), a && a.data && (o.data = a.data, a.data.jstree)) for (f in a.data.jstree) a.data.jstree.hasOwnProperty(f) && (o.state[f] = a.data.jstree[f]);
                                if (a && "object" == typeof a.state) for (f in a.state) a.state.hasOwnProperty(f) && (o.state[f] = a.state[f]);
                                if (a && "object" == typeof a.li_attr) for (f in a.li_attr) a.li_attr.hasOwnProperty(f) && (o.li_attr[f] = a.li_attr[f]);
                                if (o.li_attr.id && !o.id && (o.id = o.li_attr.id.toString()), o.id || (o.id = e), o.li_attr.id || (o.li_attr.id = o.id), a && "object" == typeof a.a_attr) for (f in a.a_attr) a.a_attr.hasOwnProperty(f) && (o.a_attr[f] = a.a_attr[f]);
                                if (a && a.children && a.children.length) {
                                    for (f = 0, l = a.children.length; l > f; f++) m = s(a.children[f], o.id, d), n = k[m], o.children.push(m), n.children_d.length && (o.children_d = o.children_d.concat(n.children_d));
                                    o.children_d = o.children_d.concat(o.children)
                                }
                                return a && a.children && a.children === !0 && (o.state.loaded = !1, o.children = [], o.children_d = []), delete a.data, delete a.children, o.original = a, k[o.id] = o, o.state.selected && g.push(o.id), o.id
                            };
                        if (c.length && c[0].id !== b && c[0].parent !== b) {
                            for (o = 0, p = c.length; p > o; o++) c[o].children || (c[o].children = []), k[c[o].id.toString()] = c[o];
                            for (o = 0, p = c.length; p > o; o++) k[c[o].parent.toString()].children.push(c[o].id.toString()), l.children_d.push(c[o].id.toString());
                            for (o = 0, p = l.children.length; p > o; o++) n = r(k[l.children[o]], d, l.parents.concat()), f.push(n), k[n].children_d.length && (f = f.concat(k[n].children_d));
                            for (o = 0, p = l.parents.length; p > o; o++) k[l.parents[o]].children_d = k[l.parents[o]].children_d.concat(f);
                            q = {cnt: j, mod: k, sel: m, par: d, dpc: f, add: g}
                        } else {
                            for (o = 0, p = c.length; p > o; o++) n = s(c[o], d, l.parents.concat()), n && (e.push(n), f.push(n), k[n].children_d.length && (f = f.concat(k[n].children_d)));
                            for (l.children = e, l.children_d = f, o = 0, p = l.parents.length; p > o; o++) k[l.parents[o]].children_d = k[l.parents[o]].children_d.concat(f);
                            q = {cnt: j, mod: k, sel: m, par: d, dpc: f, add: g}
                        }
                        return "undefined" != typeof window && "undefined" != typeof window.document ? q : void postMessage(q)
                    }, i = function (b, c) {
                        if (this._cnt = b.cnt, this._model.data = b.mod, c) {
                            var e, f, g = b.add, h = b.sel, i = this._data.core.selected.slice(), j = this._model.data;
                            if (h.length !== i.length || a.vakata.array_unique(h.concat(i)).length !== h.length) {
                                for (e = 0, f = h.length; f > e; e++) -1 === a.inArray(h[e], g) && -1 === a.inArray(h[e], i) && (j[h[e]].state.selected = !1);
                                for (e = 0, f = i.length; f > e; e++) -1 === a.inArray(i[e], h) && (j[i[e]].state.selected = !0)
                            }
                        }
                        b.add.length && (this._data.core.selected = this._data.core.selected.concat(b.add)), this.trigger("model", {
                            nodes: b.dpc,
                            parent: b.par
                        }), "#" !== b.par ? (this._node_changed(b.par), this.redraw()) : this.redraw(!0), b.add.length && this.trigger("changed", {
                            action: "model",
                            selected: this._data.core.selected
                        }), d.call(this, !0)
                    };
                    if (this.settings.core.worker && window.Blob && window.URL && window.Worker) try {
                        null === this._wrk && (this._wrk = window.URL.createObjectURL(new window.Blob(["self.onmessage = " + h.toString()], {type: "text/javascript"}))), !this._data.core.working || e ? (this._data.core.working = !0, f = new window.Worker(this._wrk), f.onmessage = a.proxy(function (a) {
                            i.call(this, a.data, !0);
                            try {
                                f.terminate(), f = null
                            } catch (b) {
                            }
                            this._data.core.worker_queue.length ? this._append_json_data.apply(this, this._data.core.worker_queue.shift()) : this._data.core.working = !1
                        }, this), g.par ? f.postMessage(g) : this._data.core.worker_queue.length ? this._append_json_data.apply(this, this._data.core.worker_queue.shift()) : this._data.core.working = !1) : this._data.core.worker_queue.push([b, c, d, !0])
                    } catch (j) {
                        i.call(this, h(g), !1), this._data.core.worker_queue.length ? this._append_json_data.apply(this, this._data.core.worker_queue.shift()) : this._data.core.working = !1
                    } else i.call(this, h(g), !1)
                }, _parse_model_from_html: function (b, c, d) {
                    d = d ? [].concat(d) : [], c && d.unshift(c);
                    var e, f, g = this._model.data, h = {
                        id: !1,
                        text: !1,
                        icon: !0,
                        parent: c,
                        parents: d,
                        children: [],
                        children_d: [],
                        data: null,
                        state: {},
                        li_attr: {id: !1},
                        a_attr: {href: "#"},
                        original: !1
                    }, i, j, k;
                    for (i in this._model.default_state) this._model.default_state.hasOwnProperty(i) && (h.state[i] = this._model.default_state[i]);
                    if (j = a.vakata.attributes(b, !0), a.each(j, function (b, c) {
                        return c = a.trim(c), c.length ? (h.li_attr[b] = c, void ("id" === b && (h.id = c.toString()))) : !0
                    }), j = b.children("a").first(), j.length && (j = a.vakata.attributes(j, !0), a.each(j, function (b, c) {
                        c = a.trim(c), c.length && (h.a_attr[b] = c)
                    })), j = b.children("a").first().length ? b.children("a").first().clone() : b.clone(), j.children("ins, i, ul").remove(), j = j.html(), j = a("<div />").html(j), h.text = this.settings.core.force_text ? j.text() : j.html(), j = b.data(), h.data = j ? a.extend(!0, {}, j) : null, h.state.opened = b.hasClass("jstree-open"), h.state.selected = b.children("a").hasClass("jstree-clicked"), h.state.disabled = b.children("a").hasClass("jstree-disabled"), h.data && h.data.jstree) for (i in h.data.jstree) h.data.jstree.hasOwnProperty(i) && (h.state[i] = h.data.jstree[i]);
                    j = b.children("a").children(".jstree-themeicon"), j.length && (h.icon = j.hasClass("jstree-themeicon-hidden") ? !1 : j.attr("rel")), h.state.icon && (h.icon = h.state.icon), j = b.children("ul").children("li");
                    do k = "j" + this._id + "_" + ++this._cnt; while (g[k]);
                    return h.id = h.li_attr.id ? h.li_attr.id.toString() : k, j.length ? (j.each(a.proxy(function (b, c) {
                        e = this._parse_model_from_html(a(c), h.id, d), f = this._model.data[e], h.children.push(e), f.children_d.length && (h.children_d = h.children_d.concat(f.children_d))
                    }, this)), h.children_d = h.children_d.concat(h.children)) : b.hasClass("jstree-closed") && (h.state.loaded = !1), h.li_attr["class"] && (h.li_attr["class"] = h.li_attr["class"].replace("jstree-closed", "").replace("jstree-open", "")), h.a_attr["class"] && (h.a_attr["class"] = h.a_attr["class"].replace("jstree-clicked", "").replace("jstree-disabled", "")), g[h.id] = h, h.state.selected && this._data.core.selected.push(h.id), h.id
                }, _parse_model_from_flat_json: function (a, c, d) {
                    d = d ? d.concat() : [], c && d.unshift(c);
                    var e = a.id.toString(), f = this._model.data, g = this._model.default_state, h, i, j, k, l = {
                        id: e,
                        text: a.text || "",
                        icon: a.icon !== b ? a.icon : !0,
                        parent: c,
                        parents: d,
                        children: a.children || [],
                        children_d: a.children_d || [],
                        data: a.data,
                        state: {},
                        li_attr: {id: !1},
                        a_attr: {href: "#"},
                        original: !1
                    };
                    for (h in g) g.hasOwnProperty(h) && (l.state[h] = g[h]);
                    if (a && a.data && a.data.jstree && a.data.jstree.icon && (l.icon = a.data.jstree.icon), a && a.data && (l.data = a.data, a.data.jstree)) for (h in a.data.jstree) a.data.jstree.hasOwnProperty(h) && (l.state[h] = a.data.jstree[h]);
                    if (a && "object" == typeof a.state) for (h in a.state) a.state.hasOwnProperty(h) && (l.state[h] = a.state[h]);
                    if (a && "object" == typeof a.li_attr) for (h in a.li_attr) a.li_attr.hasOwnProperty(h) && (l.li_attr[h] = a.li_attr[h]);
                    if (l.li_attr.id || (l.li_attr.id = e), a && "object" == typeof a.a_attr) for (h in a.a_attr) a.a_attr.hasOwnProperty(h) && (l.a_attr[h] = a.a_attr[h]);
                    for (a && a.children && a.children === !0 && (l.state.loaded = !1, l.children = [], l.children_d = []), f[l.id] = l, h = 0, i = l.children.length; i > h; h++) j = this._parse_model_from_flat_json(f[l.children[h]], l.id, d), k = f[j], l.children_d.push(j), k.children_d.length && (l.children_d = l.children_d.concat(k.children_d));
                    return delete a.data, delete a.children, f[l.id].original = a, l.state.selected && this._data.core.selected.push(l.id), l.id
                }, _parse_model_from_json: function (a, c, d) {
                    d = d ? d.concat() : [], c && d.unshift(c);
                    var e = !1, f, g, h, i, j = this._model.data, k = this._model.default_state, l;
                    do e = "j" + this._id + "_" + ++this._cnt; while (j[e]);
                    l = {
                        id: !1,
                        text: "string" == typeof a ? a : "",
                        icon: "object" == typeof a && a.icon !== b ? a.icon : !0,
                        parent: c,
                        parents: d,
                        children: [],
                        children_d: [],
                        data: null,
                        state: {},
                        li_attr: {id: !1},
                        a_attr: {href: "#"},
                        original: !1
                    };
                    for (f in k) k.hasOwnProperty(f) && (l.state[f] = k[f]);
                    if (a && a.id && (l.id = a.id.toString()), a && a.text && (l.text = a.text), a && a.data && a.data.jstree && a.data.jstree.icon && (l.icon = a.data.jstree.icon), a && a.data && (l.data = a.data, a.data.jstree)) for (f in a.data.jstree) a.data.jstree.hasOwnProperty(f) && (l.state[f] = a.data.jstree[f]);
                    if (a && "object" == typeof a.state) for (f in a.state) a.state.hasOwnProperty(f) && (l.state[f] = a.state[f]);
                    if (a && "object" == typeof a.li_attr) for (f in a.li_attr) a.li_attr.hasOwnProperty(f) && (l.li_attr[f] = a.li_attr[f]);
                    if (l.li_attr.id && !l.id && (l.id = l.li_attr.id.toString()), l.id || (l.id = e), l.li_attr.id || (l.li_attr.id = l.id), a && "object" == typeof a.a_attr) for (f in a.a_attr) a.a_attr.hasOwnProperty(f) && (l.a_attr[f] = a.a_attr[f]);
                    if (a && a.children && a.children.length) {
                        for (f = 0, g = a.children.length; g > f; f++) h = this._parse_model_from_json(a.children[f], l.id, d), i = j[h], l.children.push(h), i.children_d.length && (l.children_d = l.children_d.concat(i.children_d));
                        l.children_d = l.children_d.concat(l.children)
                    }
                    return a && a.children && a.children === !0 && (l.state.loaded = !1, l.children = [], l.children_d = []), delete a.data, delete a.children, l.original = a, j[l.id] = l, l.state.selected && this._data.core.selected.push(l.id), l.id
                }, _redraw: function () {
                    var a = this._model.force_full_redraw ? this._model.data["#"].children.concat([]) : this._model.changed.concat([]),
                        b = document.createElement("UL"), c, d, e, f = this._data.core.focused;
                    for (d = 0, e = a.length; e > d; d++) c = this.redraw_node(a[d], !0, this._model.force_full_redraw), c && this._model.force_full_redraw && b.appendChild(c);
                    this._model.force_full_redraw && (b.className = this.get_container_ul()[0].className, b.setAttribute("role", "group"), this.element.empty().append(b)), null !== f && (c = this.get_node(f, !0), c && c.length && c.children(".jstree-anchor")[0] !== document.activeElement ? c.children(".jstree-anchor").focus() : this._data.core.focused = null), this._model.force_full_redraw = !1, this._model.changed = [], this.trigger("redraw", {nodes: a})
                }, redraw: function (a) {
                    a && (this._model.force_full_redraw = !0), this._redraw()
                }, draw_children: function (a) {
                    var b = this.get_node(a), c = !1, d = !1, e = !1, f = document;
                    if (!b) return !1;
                    if ("#" === b.id) return this.redraw(!0);
                    if (a = this.get_node(a, !0), !a || !a.length) return !1;
                    if (a.children(".jstree-children").remove(), a = a[0], b.children.length && b.state.loaded) {
                        for (e = f.createElement("UL"), e.setAttribute("role", "group"), e.className = "jstree-children", c = 0, d = b.children.length; d > c; c++) e.appendChild(this.redraw_node(b.children[c], !0, !0));
                        a.appendChild(e)
                    }
                }, redraw_node: function (b, c, d, e) {
                    var f = this.get_node(b), g = !1, h = !1, i = !1, k = !1, l = !1, m = !1, n = "", o = document,
                        p = this._model.data, q = !1, r = !1, s = null, t = 0, u = 0;
                    if (!f) return !1;
                    if ("#" === f.id) return this.redraw(!0);
                    if (c = c || 0 === f.children.length, b = document.querySelector ? this.element[0].querySelector("#" + (-1 !== "0123456789".indexOf(f.id[0]) ? "\\3" + f.id[0] + " " + f.id.substr(1).replace(a.jstree.idregex, "\\$&") : f.id.replace(a.jstree.idregex, "\\$&"))) : document.getElementById(f.id)) b = a(b), d || (g = b.parent().parent()[0], g === this.element[0] && (g = null), h = b.index()), c || !f.children.length || b.children(".jstree-children").length || (c = !0), c || (i = b.children(".jstree-children")[0]), q = b.children(".jstree-anchor")[0] === document.activeElement, b.remove(); else if (c = !0, !d) {
                        if (g = "#" !== f.parent ? a("#" + f.parent.replace(a.jstree.idregex, "\\$&"), this.element)[0] : null, !(null === g || g && p[f.parent].state.opened)) return !1;
                        h = a.inArray(f.id, null === g ? p["#"].children : p[f.parent].children)
                    }
                    b = j.cloneNode(!0), n = "jstree-node ";
                    for (k in f.li_attr) if (f.li_attr.hasOwnProperty(k)) {
                        if ("id" === k) continue;
                        "class" !== k ? b.setAttribute(k, f.li_attr[k]) : n += f.li_attr[k]
                    }
                    f.a_attr.id || (f.a_attr.id = f.id + "_anchor"), b.setAttribute("aria-selected", !!f.state.selected), b.setAttribute("aria-level", f.parents.length), b.setAttribute("aria-labelledby", f.a_attr.id), f.state.disabled && b.setAttribute("aria-disabled", !0), f.state.loaded && !f.children.length ? n += " jstree-leaf" : (n += f.state.opened && f.state.loaded ? " jstree-open" : " jstree-closed", b.setAttribute("aria-expanded", f.state.opened && f.state.loaded)), null !== f.parent && p[f.parent].children[p[f.parent].children.length - 1] === f.id && (n += " jstree-last"), b.id = f.id, b.className = n, n = (f.state.selected ? " jstree-clicked" : "") + (f.state.disabled ? " jstree-disabled" : "");
                    for (l in f.a_attr) if (f.a_attr.hasOwnProperty(l)) {
                        if ("href" === l && "#" === f.a_attr[l]) continue;
                        "class" !== l ? b.childNodes[1].setAttribute(l, f.a_attr[l]) : n += " " + f.a_attr[l]
                    }
                    if (n.length && (b.childNodes[1].className = "jstree-anchor " + n), (f.icon && f.icon !== !0 || f.icon === !1) && (f.icon === !1 ? b.childNodes[1].childNodes[0].className += " jstree-themeicon-hidden" : -1 === f.icon.indexOf("/") && -1 === f.icon.indexOf(".") ? b.childNodes[1].childNodes[0].className += " " + f.icon + " jstree-themeicon-custom" : (b.childNodes[1].childNodes[0].style.backgroundImage = "url(" + f.icon + ")", b.childNodes[1].childNodes[0].style.backgroundPosition = "center center", b.childNodes[1].childNodes[0].style.backgroundSize = "auto", b.childNodes[1].childNodes[0].className += " jstree-themeicon-custom")), this.settings.core.force_text ? b.childNodes[1].appendChild(o.createTextNode(f.text)) : b.childNodes[1].innerHTML += f.text, c && f.children.length && (f.state.opened || e) && f.state.loaded) {
                        for (m = o.createElement("UL"), m.setAttribute("role", "group"), m.className = "jstree-children", k = 0, l = f.children.length; l > k; k++) m.appendChild(this.redraw_node(f.children[k], c, !0));
                        b.appendChild(m)
                    }
                    if (i && b.appendChild(i), !d) {
                        for (g || (g = this.element[0]), k = 0, l = g.childNodes.length; l > k; k++) if (g.childNodes[k] && g.childNodes[k].className && -1 !== g.childNodes[k].className.indexOf("jstree-children")) {
                            s = g.childNodes[k];
                            break
                        }
                        s || (s = o.createElement("UL"), s.setAttribute("role", "group"), s.className = "jstree-children", g.appendChild(s)), g = s, h < g.childNodes.length ? g.insertBefore(b, g.childNodes[h]) : g.appendChild(b), q && (t = this.element[0].scrollTop, u = this.element[0].scrollLeft, b.childNodes[1].focus(), this.element[0].scrollTop = t, this.element[0].scrollLeft = u)
                    }
                    return f.state.opened && !f.state.loaded && (f.state.opened = !1, setTimeout(a.proxy(function () {
                        this.open_node(f.id, !1, 0)
                    }, this), 0)), b
                }, open_node: function (c, d, e) {
                    var f, g, h, i;
                    if (a.isArray(c)) {
                        for (c = c.slice(), f = 0, g = c.length; g > f; f++) this.open_node(c[f], d, e);
                        return !0
                    }
                    if (c = this.get_node(c), !c || "#" === c.id) return !1;
                    if (e = e === b ? this.settings.core.animation : e, !this.is_closed(c)) return d && d.call(this, c, !1), !1;
                    if (this.is_loaded(c)) h = this.get_node(c, !0), i = this, h.length && (e && h.children(".jstree-children").length && h.children(".jstree-children").stop(!0, !0), c.children.length && !this._firstChild(h.children(".jstree-children")[0]) && this.draw_children(c), e ? (this.trigger("before_open", {node: c}), h.children(".jstree-children").css("display", "none").end().removeClass("jstree-closed").addClass("jstree-open").attr("aria-expanded", !0).children(".jstree-children").stop(!0, !0).slideDown(e, function () {
                        this.style.display = "", i.trigger("after_open", {node: c})
                    })) : (this.trigger("before_open", {node: c}), h[0].className = h[0].className.replace("jstree-closed", "jstree-open"), h[0].setAttribute("aria-expanded", !0))), c.state.opened = !0, d && d.call(this, c, !0), h.length || this.trigger("before_open", {node: c}), this.trigger("open_node", {node: c}), e && h.length || this.trigger("after_open", {node: c}); else {
                        if (this.is_loading(c)) return setTimeout(a.proxy(function () {
                            this.open_node(c, d, e)
                        }, this), 500);
                        this.load_node(c, function (a, b) {
                            return b ? this.open_node(a, d, e) : d ? d.call(this, a, !1) : !1
                        })
                    }
                }, _open_to: function (b) {
                    if (b = this.get_node(b), !b || "#" === b.id) return !1;
                    var c, d, e = b.parents;
                    for (c = 0, d = e.length; d > c; c += 1) "#" !== c && this.open_node(e[c], !1, 0);
                    return a("#" + b.id.replace(a.jstree.idregex, "\\$&"), this.element)
                }, close_node: function (c, d) {
                    var e, f, g, h;
                    if (a.isArray(c)) {
                        for (c = c.slice(), e = 0, f = c.length; f > e; e++) this.close_node(c[e], d);
                        return !0
                    }
                    return c = this.get_node(c), c && "#" !== c.id ? this.is_closed(c) ? !1 : (d = d === b ? this.settings.core.animation : d, g = this, h = this.get_node(c, !0), h.length && (d ? h.children(".jstree-children").attr("style", "display:block !important").end().removeClass("jstree-open").addClass("jstree-closed").attr("aria-expanded", !1).children(".jstree-children").stop(!0, !0).slideUp(d, function () {
                        this.style.display = "", h.children(".jstree-children").remove(), g.trigger("after_close", {node: c})
                    }) : (h[0].className = h[0].className.replace("jstree-open", "jstree-closed"), h.attr("aria-expanded", !1).children(".jstree-children").remove())), c.state.opened = !1, this.trigger("close_node", {node: c}), void (d && h.length || this.trigger("after_close", {node: c}))) : !1
                }, toggle_node: function (b) {
                    var c, d;
                    if (a.isArray(b)) {
                        for (b = b.slice(), c = 0, d = b.length; d > c; c++) this.toggle_node(b[c]);
                        return !0
                    }
                    return this.is_closed(b) ? this.open_node(b) : this.is_open(b) ? this.close_node(b) : void 0
                }, open_all: function (a, b, c) {
                    if (a || (a = "#"), a = this.get_node(a), !a) return !1;
                    var d = "#" === a.id ? this.get_container_ul() : this.get_node(a, !0), e, f, g;
                    if (!d.length) {
                        for (e = 0, f = a.children_d.length; f > e; e++) this.is_closed(this._model.data[a.children_d[e]]) && (this._model.data[a.children_d[e]].state.opened = !0);
                        return this.trigger("open_all", {node: a})
                    }
                    c = c || d, g = this, d = this.is_closed(a) ? d.find(".jstree-closed").addBack() : d.find(".jstree-closed"), d.each(function () {
                        g.open_node(this, function (a, d) {
                            d && this.is_parent(a) && this.open_all(a, b, c)
                        }, b || 0)
                    }), 0 === c.find(".jstree-closed").length && this.trigger("open_all", {node: this.get_node(c)})
                }, close_all: function (b, c) {
                    if (b || (b = "#"), b = this.get_node(b), !b) return !1;
                    var d = "#" === b.id ? this.get_container_ul() : this.get_node(b, !0), e = this, f, g;
                    if (!d.length) {
                        for (f = 0, g = b.children_d.length; g > f; f++) this._model.data[b.children_d[f]].state.opened = !1;
                        return this.trigger("close_all", {node: b})
                    }
                    d = this.is_open(b) ? d.find(".jstree-open").addBack() : d.find(".jstree-open"), a(d.get().reverse()).each(function () {
                        e.close_node(this, c || 0)
                    }), this.trigger("close_all", {node: b})
                }, is_disabled: function (a) {
                    return a = this.get_node(a), a && a.state && a.state.disabled
                }, enable_node: function (b) {
                    var c, d;
                    if (a.isArray(b)) {
                        for (b = b.slice(), c = 0, d = b.length; d > c; c++) this.enable_node(b[c]);
                        return !0
                    }
                    return b = this.get_node(b), b && "#" !== b.id ? (b.state.disabled = !1, this.get_node(b, !0).children(".jstree-anchor").removeClass("jstree-disabled").attr("aria-disabled", !1), void this.trigger("enable_node", {node: b})) : !1
                }, disable_node: function (b) {
                    var c, d;
                    if (a.isArray(b)) {
                        for (b = b.slice(), c = 0, d = b.length; d > c; c++) this.disable_node(b[c]);
                        return !0
                    }
                    return b = this.get_node(b), b && "#" !== b.id ? (b.state.disabled = !0, this.get_node(b, !0).children(".jstree-anchor").addClass("jstree-disabled").attr("aria-disabled", !0), void this.trigger("disable_node", {node: b})) : !1
                }, activate_node: function (a, c) {
                    if (this.is_disabled(a)) return !1;
                    if (this._data.core.last_clicked = this._data.core.last_clicked && this._data.core.last_clicked.id !== b ? this.get_node(this._data.core.last_clicked.id) : null, this._data.core.last_clicked && !this._data.core.last_clicked.state.selected && (this._data.core.last_clicked = null), !this._data.core.last_clicked && this._data.core.selected.length && (this._data.core.last_clicked = this.get_node(this._data.core.selected[this._data.core.selected.length - 1])), this.settings.core.multiple && (c.metaKey || c.ctrlKey || c.shiftKey) && (!c.shiftKey || this._data.core.last_clicked && this.get_parent(a) && this.get_parent(a) === this._data.core.last_clicked.parent)) if (c.shiftKey) {
                        var d = this.get_node(a).id, e = this._data.core.last_clicked.id,
                            f = this.get_node(this._data.core.last_clicked.parent).children, g = !1, h, i;
                        for (h = 0, i = f.length; i > h; h += 1) f[h] === d && (g = !g), f[h] === e && (g = !g), g || f[h] === d || f[h] === e ? this.select_node(f[h], !0, !1, c) : this.deselect_node(f[h], !0, c);
                        this.trigger("changed", {
                            action: "select_node",
                            node: this.get_node(a),
                            selected: this._data.core.selected,
                            event: c
                        })
                    } else this.is_selected(a) ? this.deselect_node(a, !1, c) : this.select_node(a, !1, !1, c); else !this.settings.core.multiple && (c.metaKey || c.ctrlKey || c.shiftKey) && this.is_selected(a) ? this.deselect_node(a, !1, c) : (this.deselect_all(!0), this.select_node(a, !1, !1, c), this._data.core.last_clicked = this.get_node(a));
                    this.trigger("activate_node", {node: this.get_node(a)})
                }, hover_node: function (a) {
                    if (a = this.get_node(a, !0), !a || !a.length || a.children(".jstree-hovered").length) return !1;
                    var b = this.element.find(".jstree-hovered"), c = this.element;
                    b && b.length && this.dehover_node(b), a.children(".jstree-anchor").addClass("jstree-hovered"), this.trigger("hover_node", {node: this.get_node(a)}), setTimeout(function () {
                        c.attr("aria-activedescendant", a[0].id)
                    }, 0)
                }, dehover_node: function (a) {
                    return a = this.get_node(a, !0), a && a.length && a.children(".jstree-hovered").length ? (a.children(".jstree-anchor").removeClass("jstree-hovered"), void this.trigger("dehover_node", {node: this.get_node(a)})) : !1
                }, select_node: function (b, c, d, e) {
                    var f, g, h, i;
                    if (a.isArray(b)) {
                        for (b = b.slice(), g = 0, h = b.length; h > g; g++) this.select_node(b[g], c, d, e);
                        return !0
                    }
                    return b = this.get_node(b), b && "#" !== b.id ? (f = this.get_node(b, !0), void (b.state.selected || (b.state.selected = !0, this._data.core.selected.push(b.id), d || (f = this._open_to(b)), f && f.length && f.attr("aria-selected", !0).children(".jstree-anchor").addClass("jstree-clicked"), this.trigger("select_node", {
                        node: b,
                        selected: this._data.core.selected,
                        event: e
                    }), c || this.trigger("changed", {
                        action: "select_node",
                        node: b,
                        selected: this._data.core.selected,
                        event: e
                    })))) : !1
                }, deselect_node: function (b, c, d) {
                    var e, f, g;
                    if (a.isArray(b)) {
                        for (b = b.slice(), e = 0, f = b.length; f > e; e++) this.deselect_node(b[e], c, d);
                        return !0
                    }
                    return b = this.get_node(b), b && "#" !== b.id ? (g = this.get_node(b, !0), void (b.state.selected && (b.state.selected = !1, this._data.core.selected = a.vakata.array_remove_item(this._data.core.selected, b.id), g.length && g.attr("aria-selected", !1).children(".jstree-anchor").removeClass("jstree-clicked"), this.trigger("deselect_node", {
                        node: b,
                        selected: this._data.core.selected,
                        event: d
                    }), c || this.trigger("changed", {
                        action: "deselect_node",
                        node: b,
                        selected: this._data.core.selected,
                        event: d
                    })))) : !1
                }, select_all: function (a) {
                    var b = this._data.core.selected.concat([]), c, d;
                    for (this._data.core.selected = this._model.data["#"].children_d.concat(), c = 0, d = this._data.core.selected.length; d > c; c++) this._model.data[this._data.core.selected[c]] && (this._model.data[this._data.core.selected[c]].state.selected = !0);
                    this.redraw(!0), this.trigger("select_all", {selected: this._data.core.selected}), a || this.trigger("changed", {
                        action: "select_all",
                        selected: this._data.core.selected,
                        old_selection: b
                    })
                }, deselect_all: function (a) {
                    var b = this._data.core.selected.concat([]), c, d;
                    for (c = 0, d = this._data.core.selected.length; d > c; c++) this._model.data[this._data.core.selected[c]] && (this._model.data[this._data.core.selected[c]].state.selected = !1);
                    this._data.core.selected = [], this.element.find(".jstree-clicked").removeClass("jstree-clicked").parent().attr("aria-selected", !1), this.trigger("deselect_all", {
                        selected: this._data.core.selected,
                        node: b
                    }), a || this.trigger("changed", {
                        action: "deselect_all",
                        selected: this._data.core.selected,
                        old_selection: b
                    })
                }, is_selected: function (a) {
                    return a = this.get_node(a), a && "#" !== a.id ? a.state.selected : !1
                }, get_selected: function (b) {
                    return b ? a.map(this._data.core.selected, a.proxy(function (a) {
                        return this.get_node(a)
                    }, this)) : this._data.core.selected.slice()
                }, get_top_selected: function (b) {
                    var c = this.get_selected(!0), d = {}, e, f, g, h;
                    for (e = 0, f = c.length; f > e; e++) d[c[e].id] = c[e];
                    for (e = 0, f = c.length; f > e; e++) for (g = 0, h = c[e].children_d.length; h > g; g++) d[c[e].children_d[g]] && delete d[c[e].children_d[g]];
                    c = [];
                    for (e in d) d.hasOwnProperty(e) && c.push(e);
                    return b ? a.map(c, a.proxy(function (a) {
                        return this.get_node(a)
                    }, this)) : c
                }, get_bottom_selected: function (b) {
                    var c = this.get_selected(!0), d = [], e, f;
                    for (e = 0, f = c.length; f > e; e++) c[e].children.length || d.push(c[e].id);
                    return b ? a.map(d, a.proxy(function (a) {
                        return this.get_node(a)
                    }, this)) : d
                }, get_state: function () {
                    var a = {
                        core: {
                            open: [],
                            scroll: {left: this.element.scrollLeft(), top: this.element.scrollTop()},
                            selected: []
                        }
                    }, b;
                    for (b in this._model.data) this._model.data.hasOwnProperty(b) && "#" !== b && (this._model.data[b].state.opened && a.core.open.push(b), this._model.data[b].state.selected && a.core.selected.push(b));
                    return a
                }, set_state: function (c, d) {
                    if (c) {
                        if (c.core) {
                            var e, f, g, h;
                            if (c.core.open) return a.isArray(c.core.open) ? (e = !0, f = !1, g = this, a.each(c.core.open.concat([]), function (b, h) {
                                f = g.get_node(h), f && (g.is_loaded(h) ? (g.is_closed(h) && g.open_node(h, !1, 0), c && c.core && c.core.open && a.vakata.array_remove_item(c.core.open, h)) : (g.is_loading(h) || g.open_node(h, a.proxy(function (b, e) {
                                    !e && c && c.core && c.core.open && a.vakata.array_remove_item(c.core.open, b.id), this.set_state(c, d)
                                }, g), 0), e = !1))
                            }), e && (delete c.core.open, this.set_state(c, d)), !1) : (delete c.core.open, this.set_state(c, d), !1);
                            if (c.core.scroll) return c.core.scroll && c.core.scroll.left !== b && this.element.scrollLeft(c.core.scroll.left), c.core.scroll && c.core.scroll.top !== b && this.element.scrollTop(c.core.scroll.top), delete c.core.scroll, this.set_state(c, d), !1;
                            if (c.core.selected) return h = this, this.deselect_all(), a.each(c.core.selected, function (a, b) {
                                h.select_node(b)
                            }), delete c.core.selected, this.set_state(c, d), !1;
                            if (a.isEmptyObject(c.core)) return delete c.core, this.set_state(c, d), !1
                        }
                        return a.isEmptyObject(c) ? (c = null, d && d.call(this), this.trigger("set_state"), !1) : !0
                    }
                    return !1
                }, refresh: function (b, c) {
                    this._data.core.state = c === !0 ? {} : this.get_state(), c && a.isFunction(c) && (this._data.core.state = c.call(this, this._data.core.state)), this._cnt = 0, this._model.data = {
                        "#": {
                            id: "#",
                            parent: null,
                            parents: [],
                            children: [],
                            children_d: [],
                            state: {loaded: !1}
                        }
                    };
                    var d = this.get_container_ul()[0].className;
                    b || (this.element.html("<ul class='" + d + "' role='group'><li class='jstree-initial-node jstree-loading jstree-leaf jstree-last' role='treeitem' id='j" + this._id + "_loading'><i class='jstree-icon jstree-ocl'></i><a class='jstree-anchor' href='#'><i class='jstree-icon jstree-themeicon-hidden'></i>" + this.get_string("Loading ...") + "</a></li></ul>"), this.element.attr("aria-activedescendant", "j" + this._id + "_loading")), this.load_node("#", function (b, c) {
                        c && (this.get_container_ul()[0].className = d, this._firstChild(this.get_container_ul()[0]) && this.element.attr("aria-activedescendant", this._firstChild(this.get_container_ul()[0]).id), this.set_state(a.extend(!0, {}, this._data.core.state), function () {
                            this.trigger("refresh")
                        })), this._data.core.state = null
                    })
                }, refresh_node: function (b) {
                    if (b = this.get_node(b), !b || "#" === b.id) return !1;
                    var c = [], d = [], e = this._data.core.selected.concat([]);
                    d.push(b.id), b.state.opened === !0 && c.push(b.id), this.get_node(b, !0).find(".jstree-open").each(function () {
                        c.push(this.id)
                    }), this._load_nodes(d, a.proxy(function (a) {
                        this.open_node(c, !1, 0), this.select_node(this._data.core.selected), this.trigger("refresh_node", {
                            node: b,
                            nodes: a
                        })
                    }, this))
                }, set_id: function (b, c) {
                    if (b = this.get_node(b), !b || "#" === b.id) return !1;
                    var d, e, f = this._model.data;
                    for (c = c.toString(), f[b.parent].children[a.inArray(b.id, f[b.parent].children)] = c, d = 0, e = b.parents.length; e > d; d++) f[b.parents[d]].children_d[a.inArray(b.id, f[b.parents[d]].children_d)] = c;
                    for (d = 0, e = b.children.length; e > d; d++) f[b.children[d]].parent = c;
                    for (d = 0, e = b.children_d.length; e > d; d++) f[b.children_d[d]].parents[a.inArray(b.id, f[b.children_d[d]].parents)] = c;
                    return d = a.inArray(b.id, this._data.core.selected), -1 !== d && (this._data.core.selected[d] = c), d = this.get_node(b.id, !0), d && d.attr("id", c), delete f[b.id], b.id = c, f[c] = b, !0
                }, get_text: function (a) {
                    return a = this.get_node(a), a && "#" !== a.id ? a.text : !1
                }, set_text: function (b, c) {
                    var d, e;
                    if (a.isArray(b)) {
                        for (b = b.slice(), d = 0, e = b.length; e > d; d++) this.set_text(b[d], c);
                        return !0
                    }
                    return b = this.get_node(b), b && "#" !== b.id ? (b.text = c, this.get_node(b, !0).length && this.redraw_node(b.id), this.trigger("set_text", {
                        obj: b,
                        text: c
                    }), !0) : !1
                }, get_json: function (b, c, d) {
                    if (b = this.get_node(b || "#"), !b) return !1;
                    c && c.flat && !d && (d = []);
                    var e = {
                        id: b.id,
                        text: b.text,
                        icon: this.get_icon(b),
                        li_attr: a.extend(!0, {}, b.li_attr),
                        a_attr: a.extend(!0, {}, b.a_attr),
                        state: {},
                        data: c && c.no_data ? !1 : a.extend(!0, {}, b.data)
                    }, f, g;
                    if (c && c.flat ? e.parent = b.parent : e.children = [], !c || !c.no_state) for (f in b.state) b.state.hasOwnProperty(f) && (e.state[f] = b.state[f]);
                    if (c && c.no_id && (delete e.id, e.li_attr && e.li_attr.id && delete e.li_attr.id, e.a_attr && e.a_attr.id && delete e.a_attr.id), c && c.flat && "#" !== b.id && d.push(e), !c || !c.no_children) for (f = 0, g = b.children.length; g > f; f++) c && c.flat ? this.get_json(b.children[f], c, d) : e.children.push(this.get_json(b.children[f], c));
                    return c && c.flat ? d : "#" === b.id ? e.children : e
                }, create_node: function (c, d, e, f, g) {
                    if (null === c && (c = "#"), c = this.get_node(c), !c) return !1;
                    if (e = e === b ? "last" : e, !e.toString().match(/^(before|after)$/) && !g && !this.is_loaded(c)) return this.load_node(c, function () {
                        this.create_node(c, d, e, f, !0)
                    });
                    d || (d = {text: this.get_string("New node")}), "string" == typeof d && (d = {text: d}), d.text === b && (d.text = this.get_string("New node"));
                    var h, i, j, k;
                    switch ("#" === c.id && ("before" === e && (e = "first"), "after" === e && (e = "last")), e) {
                        case"before":
                            h = this.get_node(c.parent), e = a.inArray(c.id, h.children), c = h;
                            break;
                        case"after":
                            h = this.get_node(c.parent), e = a.inArray(c.id, h.children) + 1, c = h;
                            break;
                        case"inside":
                        case"first":
                            e = 0;
                            break;
                        case"last":
                            e = c.children.length;
                            break;
                        default:
                            e || (e = 0)
                    }
                    if (e > c.children.length && (e = c.children.length), d.id || (d.id = !0), !this.check("create_node", d, c, e)) return this.settings.core.error.call(this, this._data.core.last_error), !1;
                    if (d.id === !0 && delete d.id, d = this._parse_model_from_json(d, c.id, c.parents.concat()), !d) return !1;
                    for (h = this.get_node(d), i = [], i.push(d), i = i.concat(h.children_d), this.trigger("model", {
                        nodes: i,
                        parent: c.id
                    }), c.children_d = c.children_d.concat(i), j = 0, k = c.parents.length; k > j; j++) this._model.data[c.parents[j]].children_d = this._model.data[c.parents[j]].children_d.concat(i);
                    for (d = h, h = [], j = 0, k = c.children.length; k > j; j++) h[j >= e ? j + 1 : j] = c.children[j];
                    return h[e] = d.id, c.children = h, this.redraw_node(c, !0), f && f.call(this, this.get_node(d)), this.trigger("create_node", {
                        node: this.get_node(d),
                        parent: c.id,
                        position: e
                    }), d.id
                }, rename_node: function (b, c) {
                    var d, e, f;
                    if (a.isArray(b)) {
                        for (b = b.slice(), d = 0, e = b.length; e > d; d++) this.rename_node(b[d], c);
                        return !0
                    }
                    return b = this.get_node(b), b && "#" !== b.id ? (f = b.text, this.check("rename_node", b, this.get_parent(b), c) ? (this.set_text(b, c), this.trigger("rename_node", {
                        node: b,
                        text: c,
                        old: f
                    }), !0) : (this.settings.core.error.call(this, this._data.core.last_error), !1)) : !1
                }, delete_node: function (b) {
                    var c, d, e, f, g, h, i, j, k, l;
                    if (a.isArray(b)) {
                        for (b = b.slice(), c = 0, d = b.length; d > c; c++) this.delete_node(b[c]);
                        return !0
                    }
                    if (b = this.get_node(b), !b || "#" === b.id) return !1;
                    if (e = this.get_node(b.parent), f = a.inArray(b.id, e.children), l = !1, !this.check("delete_node", b, e, f)) return this.settings.core.error.call(this, this._data.core.last_error), !1;
                    for (-1 !== f && (e.children = a.vakata.array_remove(e.children, f)), g = b.children_d.concat([]), g.push(b.id), j = 0, k = g.length; k > j; j++) {
                        for (h = 0, i = b.parents.length; i > h; h++) f = a.inArray(g[j], this._model.data[b.parents[h]].children_d), -1 !== f && (this._model.data[b.parents[h]].children_d = a.vakata.array_remove(this._model.data[b.parents[h]].children_d, f));
                        this._model.data[g[j]].state.selected && (l = !0, f = a.inArray(g[j], this._data.core.selected), -1 !== f && (this._data.core.selected = a.vakata.array_remove(this._data.core.selected, f)))
                    }
                    for (this.trigger("delete_node", {
                        node: b,
                        parent: e.id
                    }), l && this.trigger("changed", {
                        action: "delete_node",
                        node: b,
                        selected: this._data.core.selected,
                        parent: e.id
                    }), j = 0, k = g.length; k > j; j++) delete this._model.data[g[j]];
                    return this.redraw_node(e, !0), !0
                }, check: function (b, c, d, e, f) {
                    c = c && c.id ? c : this.get_node(c), d = d && d.id ? d : this.get_node(d);
                    var g = b.match(/^move_node|copy_node|create_node$/i) ? d : c,
                        h = this.settings.core.check_callback;
                    return "move_node" !== b && "copy_node" !== b || f && f.is_multi || c.id !== d.id && a.inArray(c.id, d.children) !== e && -1 === a.inArray(d.id, c.children_d) ? (g && g.data && (g = g.data), g && g.functions && (g.functions[b] === !1 || g.functions[b] === !0) ? (g.functions[b] === !1 && (this._data.core.last_error = {
                        error: "check",
                        plugin: "core",
                        id: "core_02",
                        reason: "Node data prevents function: " + b,
                        data: JSON.stringify({chk: b, pos: e, obj: c && c.id ? c.id : !1, par: d && d.id ? d.id : !1})
                    }), g.functions[b]) : h === !1 || a.isFunction(h) && h.call(this, b, c, d, e, f) === !1 || h && h[b] === !1 ? (this._data.core.last_error = {
                        error: "check",
                        plugin: "core",
                        id: "core_03",
                        reason: "User config for core.check_callback prevents function: " + b,
                        data: JSON.stringify({chk: b, pos: e, obj: c && c.id ? c.id : !1, par: d && d.id ? d.id : !1})
                    }, !1) : !0) : (this._data.core.last_error = {
                        error: "check",
                        plugin: "core",
                        id: "core_01",
                        reason: "Moving parent inside child",
                        data: JSON.stringify({chk: b, pos: e, obj: c && c.id ? c.id : !1, par: d && d.id ? d.id : !1})
                    }, !1)
                }, last_error: function () {
                    return this._data.core.last_error
                }, move_node: function (c, d, e, f, g, h) {
                    var i, j, k, l, m, n, o, p, q, r, s, t, u, v;
                    if (d = this.get_node(d), e = e === b ? 0 : e, !d) return !1;
                    if (!e.toString().match(/^(before|after)$/) && !g && !this.is_loaded(d)) return this.load_node(d, function () {
                        this.move_node(c, d, e, f, !0)
                    });
                    if (a.isArray(c)) {
                        for (c = c.slice(), i = 0, j = c.length; j > i; i++) this.move_node(c[i], d, e, f, g, !0) && (d = c[i], e = "after");
                        return this.redraw(), !0
                    }
                    if (c = c && c.id ? c : this.get_node(c), !c || "#" === c.id) return !1;
                    if (k = (c.parent || "#").toString(), m = e.toString().match(/^(before|after)$/) && "#" !== d.id ? this.get_node(d.parent) : d, n = c.instance ? c.instance : this._model.data[c.id] ? this : a.jstree.reference(c.id), o = !n || !n._id || this._id !== n._id, l = n && n._id && k && n._model.data[k] && n._model.data[k].children ? a.inArray(c.id, n._model.data[k].children) : -1, o) return this.copy_node(c, d, e, f, g) ? (n && n.delete_node(c), !0) : !1;
                    switch ("#" === d.id && ("before" === e && (e = "first"), "after" === e && (e = "last")), e) {
                        case"before":
                            e = a.inArray(d.id, m.children);
                            break;
                        case"after":
                            e = a.inArray(d.id, m.children) + 1;
                            break;
                        case"inside":
                        case"first":
                            e = 0;
                            break;
                        case"last":
                            e = m.children.length;
                            break;
                        default:
                            e || (e = 0)
                    }
                    if (e > m.children.length && (e = m.children.length), !this.check("move_node", c, m, e, {
                        core: !0,
                        is_multi: n && n._id && n._id !== this._id,
                        is_foreign: !n || !n._id
                    })) return this.settings.core.error.call(this, this._data.core.last_error), !1;
                    if (c.parent === m.id) {
                        for (p = m.children.concat(), q = a.inArray(c.id, p), -1 !== q && (p = a.vakata.array_remove(p, q), e > q && e--), q = [], r = 0, s = p.length; s > r; r++) q[r >= e ? r + 1 : r] = p[r];
                        q[e] = c.id, m.children = q, this._node_changed(m.id), this.redraw("#" === m.id)
                    } else {
                        for (q = c.children_d.concat(), q.push(c.id), r = 0, s = c.parents.length; s > r; r++) {
                            for (p = [], v = n._model.data[c.parents[r]].children_d, t = 0, u = v.length; u > t; t++) -1 === a.inArray(v[t], q) && p.push(v[t]);
                            n._model.data[c.parents[r]].children_d = p
                        }
                        for (n._model.data[k].children = a.vakata.array_remove_item(n._model.data[k].children, c.id), r = 0, s = m.parents.length; s > r; r++) this._model.data[m.parents[r]].children_d = this._model.data[m.parents[r]].children_d.concat(q);
                        for (p = [], r = 0, s = m.children.length; s > r; r++) p[r >= e ? r + 1 : r] = m.children[r];
                        for (p[e] = c.id, m.children = p, m.children_d.push(c.id), m.children_d = m.children_d.concat(c.children_d), c.parent = m.id, q = m.parents.concat(), q.unshift(m.id), v = c.parents.length, c.parents = q, q = q.concat(), r = 0, s = c.children_d.length; s > r; r++) this._model.data[c.children_d[r]].parents = this._model.data[c.children_d[r]].parents.slice(0, -1 * v), Array.prototype.push.apply(this._model.data[c.children_d[r]].parents, q);
                        ("#" === k || "#" === m.id) && (this._model.force_full_redraw = !0), this._model.force_full_redraw || (this._node_changed(k), this._node_changed(m.id)), h || this.redraw()
                    }
                    return f && f.call(this, c, m, e), this.trigger("move_node", {
                        node: c,
                        parent: m.id,
                        position: e,
                        old_parent: k,
                        old_position: l,
                        is_multi: n && n._id && n._id !== this._id,
                        is_foreign: !n || !n._id,
                        old_instance: n,
                        new_instance: this
                    }), !0
                }, copy_node: function (c, d, e, f, g, h) {
                    var i, j, k, l, m, n, o, p, q, r, s;
                    if (d = this.get_node(d), e = e === b ? 0 : e, !d) return !1;
                    if (!e.toString().match(/^(before|after)$/) && !g && !this.is_loaded(d)) return this.load_node(d, function () {
                        this.copy_node(c, d, e, f, !0)
                    });
                    if (a.isArray(c)) {
                        for (c = c.slice(), i = 0, j = c.length; j > i; i++) l = this.copy_node(c[i], d, e, f, g, !0), l && (d = l, e = "after");
                        return this.redraw(), !0
                    }
                    if (c = c && c.id ? c : this.get_node(c), !c || "#" === c.id) return !1;
                    switch (p = (c.parent || "#").toString(), q = e.toString().match(/^(before|after)$/) && "#" !== d.id ? this.get_node(d.parent) : d, r = c.instance ? c.instance : this._model.data[c.id] ? this : a.jstree.reference(c.id), s = !r || !r._id || this._id !== r._id, "#" === d.id && ("before" === e && (e = "first"), "after" === e && (e = "last")), e) {
                        case"before":
                            e = a.inArray(d.id, q.children);
                            break;
                        case"after":
                            e = a.inArray(d.id, q.children) + 1;
                            break;
                        case"inside":
                        case"first":
                            e = 0;
                            break;
                        case"last":
                            e = q.children.length;
                            break;
                        default:
                            e || (e = 0)
                    }
                    if (e > q.children.length && (e = q.children.length), !this.check("copy_node", c, q, e, {
                        core: !0,
                        is_multi: r && r._id && r._id !== this._id,
                        is_foreign: !r || !r._id
                    })) return this.settings.core.error.call(this, this._data.core.last_error), !1;
                    if (o = r ? r.get_json(c, {no_id: !0, no_data: !0, no_state: !0}) : c, !o) return !1;
                    if (o.id === !0 && delete o.id, o = this._parse_model_from_json(o, q.id, q.parents.concat()), !o) return !1;
                    for (l = this.get_node(o), c && c.state && c.state.loaded === !1 && (l.state.loaded = !1), k = [], k.push(o), k = k.concat(l.children_d), this.trigger("model", {
                        nodes: k,
                        parent: q.id
                    }), m = 0, n = q.parents.length; n > m; m++) this._model.data[q.parents[m]].children_d = this._model.data[q.parents[m]].children_d.concat(k);
                    for (k = [], m = 0, n = q.children.length; n > m; m++) k[m >= e ? m + 1 : m] = q.children[m];
                    return k[e] = l.id, q.children = k, q.children_d.push(l.id), q.children_d = q.children_d.concat(l.children_d), "#" === q.id && (this._model.force_full_redraw = !0), this._model.force_full_redraw || this._node_changed(q.id), h || this.redraw("#" === q.id), f && f.call(this, l, q, e), this.trigger("copy_node", {
                        node: l,
                        original: c,
                        parent: q.id,
                        position: e,
                        old_parent: p,
                        old_position: r && r._id && p && r._model.data[p] && r._model.data[p].children ? a.inArray(c.id, r._model.data[p].children) : -1,
                        is_multi: r && r._id && r._id !== this._id,
                        is_foreign: !r || !r._id,
                        old_instance: r,
                        new_instance: this
                    }), l.id
                }, cut: function (b) {
                    if (b || (b = this._data.core.selected.concat()), a.isArray(b) || (b = [b]), !b.length) return !1;
                    var c = [], g, h, i;
                    for (h = 0, i = b.length; i > h; h++) g = this.get_node(b[h]), g && g.id && "#" !== g.id && c.push(g);
                    return c.length ? (d = c, f = this, e = "move_node", void this.trigger("cut", {node: b})) : !1
                }, copy: function (b) {
                    if (b || (b = this._data.core.selected.concat()), a.isArray(b) || (b = [b]), !b.length) return !1;
                    var c = [], g, h, i;
                    for (h = 0, i = b.length; i > h; h++) g = this.get_node(b[h]), g && g.id && "#" !== g.id && c.push(g);
                    return c.length ? (d = c, f = this, e = "copy_node", void this.trigger("copy", {node: b})) : !1
                }, get_buffer: function () {
                    return {mode: e, node: d, inst: f}
                }, can_paste: function () {
                    return e !== !1 && d !== !1
                }, paste: function (a, b) {
                    return a = this.get_node(a), a && e && e.match(/^(copy_node|move_node)$/) && d ? (this[e](d, a, b) && this.trigger("paste", {
                        parent: a.id,
                        node: d,
                        mode: e
                    }), d = !1, e = !1, void (f = !1)) : !1
                }, clear_buffer: function () {
                    d = !1, e = !1, f = !1, this.trigger("clear_buffer")
                }, edit: function (b, c) {
                    if (b = this.get_node(b), !b) return !1;
                    if (this.settings.core.check_callback === !1) return this._data.core.last_error = {
                        error: "check",
                        plugin: "core",
                        id: "core_07",
                        reason: "Could not edit node because of check_callback"
                    }, this.settings.core.error.call(this, this._data.core.last_error), !1;
                    c = "string" == typeof c ? c : b.text, this.set_text(b, ""), b = this._open_to(b);
                    var d = this._data.core.rtl, e = this.element.width(), f = b.children(".jstree-anchor"),
                        g = a("<span>"), h = c, i = a("<div />", {
                            css: {
                                position: "absolute",
                                top: "-200px",
                                left: d ? "0px" : "-1000px",
                                visibility: "hidden"
                            }
                        }).appendTo("body"), j = a("<input />", {
                            value: h,
                            "class": "jstree-rename-input",
                            css: {
                                padding: "0",
                                border: "1px solid silver",
                                "box-sizing": "border-box",
                                display: "inline-block",
                                height: this._data.core.li_height + "px",
                                lineHeight: this._data.core.li_height + "px",
                                width: "150px"
                            },
                            blur: a.proxy(function () {
                                var c = g.children(".jstree-rename-input"), d = c.val();
                                "" === d && (d = h), i.remove(), g.replaceWith(f), g.remove(), this.set_text(b, h), this.rename_node(b, a("<div></div>").text(d)[this.settings.core.force_text ? "text" : "html"]()) === !1 && this.set_text(b, h)
                            }, this),
                            keydown: function (a) {
                                var b = a.which;
                                27 === b && (this.value = h), (27 === b || 13 === b || 37 === b || 38 === b || 39 === b || 40 === b || 32 === b) && a.stopImmediatePropagation(), (27 === b || 13 === b) && (a.preventDefault(), this.blur())
                            },
                            click: function (a) {
                                a.stopImmediatePropagation()
                            },
                            mousedown: function (a) {
                                a.stopImmediatePropagation()
                            },
                            keyup: function (a) {
                                j.width(Math.min(i.text("pW" + this.value).width(), e))
                            },
                            keypress: function (a) {
                                return 13 === a.which ? !1 : void 0
                            }
                        }), k = {
                            fontFamily: f.css("fontFamily") || "",
                            fontSize: f.css("fontSize") || "",
                            fontWeight: f.css("fontWeight") || "",
                            fontStyle: f.css("fontStyle") || "",
                            fontStretch: f.css("fontStretch") || "",
                            fontVariant: f.css("fontVariant") || "",
                            letterSpacing: f.css("letterSpacing") || "",
                            wordSpacing: f.css("wordSpacing") || ""
                        };
                    g.attr("class", f.attr("class")).append(f.contents().clone()).append(j), f.replaceWith(g), i.css(k), j.css(k).width(Math.min(i.text("pW" + j[0].value).width(), e))[0].select()
                }, set_theme: function (b, c) {
                    if (!b) return !1;
                    if (c === !0) {
                        var d = this.settings.core.themes.dir;
                        d || (d = a.jstree.path + "/themes"), c = d + "/" + b + "/style.css"
                    }
                    c && -1 === a.inArray(c, g) && (a("head").append('<link rel="stylesheet" href="' + c + '" type="text/css" />'), g.push(c)), this._data.core.themes.name && this.element.removeClass("jstree-" + this._data.core.themes.name), this._data.core.themes.name = b, this.element.addClass("jstree-" + b), this.element[this.settings.core.themes.responsive ? "addClass" : "removeClass"]("jstree-" + b + "-responsive"), this.trigger("set_theme", {theme: b})
                }, get_theme: function () {
                    return this._data.core.themes.name
                }, set_theme_variant: function (a) {
                    this._data.core.themes.variant && this.element.removeClass("jstree-" + this._data.core.themes.name + "-" + this._data.core.themes.variant), this._data.core.themes.variant = a, a && this.element.addClass("jstree-" + this._data.core.themes.name + "-" + this._data.core.themes.variant)
                }, get_theme_variant: function () {
                    return this._data.core.themes.variant
                }, show_stripes: function () {
                    this._data.core.themes.stripes = !0, this.get_container_ul().addClass("jstree-striped")
                }, hide_stripes: function () {
                    this._data.core.themes.stripes = !1, this.get_container_ul().removeClass("jstree-striped")
                }, toggle_stripes: function () {
                    this._data.core.themes.stripes ? this.hide_stripes() : this.show_stripes()
                }, show_dots: function () {
                    this._data.core.themes.dots = !0, this.get_container_ul().removeClass("jstree-no-dots")
                }, hide_dots: function () {
                    this._data.core.themes.dots = !1, this.get_container_ul().addClass("jstree-no-dots")
                }, toggle_dots: function () {
                    this._data.core.themes.dots ? this.hide_dots() : this.show_dots()
                }, show_icons: function () {
                    this._data.core.themes.icons = !0, this.get_container_ul().removeClass("jstree-no-icons")
                }, hide_icons: function () {
                    this._data.core.themes.icons = !1, this.get_container_ul().addClass("jstree-no-icons")
                }, toggle_icons: function () {
                    this._data.core.themes.icons ? this.hide_icons() : this.show_icons()
                }, set_icon: function (b, c) {
                    var d, e, f, g;
                    if (a.isArray(b)) {
                        for (b = b.slice(), d = 0, e = b.length; e > d; d++) this.set_icon(b[d], c);
                        return !0
                    }
                    return b = this.get_node(b), b && "#" !== b.id ? (g = b.icon, b.icon = c, f = this.get_node(b, !0).children(".jstree-anchor").children(".jstree-themeicon"), c === !1 ? this.hide_icon(b) : c === !0 ? (f.removeClass("jstree-themeicon-custom " + g).css("background", "").removeAttr("rel"), g === !1 && this.show_icon(b)) : -1 === c.indexOf("/") && -1 === c.indexOf(".") ? (f.removeClass(g).css("background", ""), f.addClass(c + " jstree-themeicon-custom").attr("rel", c), g === !1 && this.show_icon(b)) : (f.removeClass(g).css("background", ""), f.addClass("jstree-themeicon-custom").css("background", "url('" + c + "') center center no-repeat").attr("rel", c), g === !1 && this.show_icon(b)), !0) : !1
                }, get_icon: function (a) {
                    return a = this.get_node(a), a && "#" !== a.id ? a.icon : !1
                }, hide_icon: function (b) {
                    var c, d;
                    if (a.isArray(b)) {
                        for (b = b.slice(), c = 0, d = b.length; d > c; c++) this.hide_icon(b[c]);
                        return !0
                    }
                    return b = this.get_node(b), b && "#" !== b ? (b.icon = !1, this.get_node(b, !0).children(".jstree-anchor").children(".jstree-themeicon").addClass("jstree-themeicon-hidden"), !0) : !1
                }, show_icon: function (b) {
                    var c, d, e;
                    if (a.isArray(b)) {
                        for (b = b.slice(), c = 0, d = b.length; d > c; c++) this.show_icon(b[c]);
                        return !0
                    }
                    return b = this.get_node(b), b && "#" !== b ? (e = this.get_node(b, !0), b.icon = e.length ? e.children(".jstree-anchor").children(".jstree-themeicon").attr("rel") : !0, b.icon || (b.icon = !0), e.children(".jstree-anchor").children(".jstree-themeicon").removeClass("jstree-themeicon-hidden"), !0) : !1
                }
            }, a.vakata = {}, a.vakata.attributes = function (b, c) {
                b = a(b)[0];
                var d = c ? {} : [];
                return b && b.attributes && a.each(b.attributes, function (b, e) {
                    -1 === a.inArray(e.name.toLowerCase(), ["style", "contenteditable", "hasfocus", "tabindex"]) && null !== e.value && "" !== a.trim(e.value) && (c ? d[e.name] = e.value : d.push(e.name))
                }), d
            }, a.vakata.array_unique = function (a) {
                var b = [], c, d, e;
                for (c = 0, e = a.length; e > c; c++) {
                    for (d = 0; c >= d; d++) if (a[c] === a[d]) break;
                    d === c && b.push(a[c])
                }
                return b
            }, a.vakata.array_remove = function (a, b, c) {
                var d = a.slice((c || b) + 1 || a.length);
                return a.length = 0 > b ? a.length + b : b, a.push.apply(a, d), a
            }, a.vakata.array_remove_item = function (b, c) {
                var d = a.inArray(c, b);
                return -1 !== d ? a.vakata.array_remove(b, d) : b
            };
            var m = document.createElement("I");
            m.className = "jstree-icon jstree-checkbox", m.setAttribute("role", "presentation"), a.jstree.defaults.checkbox = {
                visible: !0,
                three_state: !0,
                whole_node: !0,
                keep_selected_style: !0,
                cascade: "",
                tie_selection: !0
            }, a.jstree.plugins.checkbox = function (b, c) {
                this.bind = function () {
                    c.bind.call(this), this._data.checkbox.uto = !1, this._data.checkbox.selected = [], this.settings.checkbox.three_state && (this.settings.checkbox.cascade = "up+down+undetermined"), this.element.on("init.jstree", a.proxy(function () {
                        this._data.checkbox.visible = this.settings.checkbox.visible, this.settings.checkbox.keep_selected_style || this.element.addClass("jstree-checkbox-no-clicked"), this.settings.checkbox.tie_selection && this.element.addClass("jstree-checkbox-selection")
                    }, this)).on("loading.jstree", a.proxy(function () {
                        this[this._data.checkbox.visible ? "show_checkboxes" : "hide_checkboxes"]()
                    }, this)), -1 !== this.settings.checkbox.cascade.indexOf("undetermined") && this.element.on("changed.jstree uncheck_node.jstree check_node.jstree uncheck_all.jstree check_all.jstree move_node.jstree copy_node.jstree redraw.jstree open_node.jstree", a.proxy(function () {
                        this._data.checkbox.uto && clearTimeout(this._data.checkbox.uto), this._data.checkbox.uto = setTimeout(a.proxy(this._undetermined, this), 50)
                    }, this)), this.settings.checkbox.tie_selection || this.element.on("model.jstree", a.proxy(function (a, b) {
                        var c = this._model.data, d = c[b.parent], e = b.nodes, f, g;
                        for (f = 0, g = e.length; g > f; f++) c[e[f]].state.checked = c[e[f]].original && c[e[f]].original.state && c[e[f]].original.state.checked, c[e[f]].state.checked && this._data.checkbox.selected.push(e[f])
                    }, this)), (-1 !== this.settings.checkbox.cascade.indexOf("up") || -1 !== this.settings.checkbox.cascade.indexOf("down")) && this.element.on("model.jstree", a.proxy(function (b, c) {
                        var d = this._model.data, e = d[c.parent], f = c.nodes, g = [], h, i, j, k, l, m,
                            n = this.settings.checkbox.cascade, o = this.settings.checkbox.tie_selection;
                        if (-1 !== n.indexOf("down")) if (e.state[o ? "selected" : "checked"]) {
                            for (i = 0, j = f.length; j > i; i++) d[f[i]].state[o ? "selected" : "checked"] = !0;
                            this._data[o ? "core" : "checkbox"].selected = this._data[o ? "core" : "checkbox"].selected.concat(f)
                        } else for (i = 0, j = f.length; j > i; i++) if (d[f[i]].state[o ? "selected" : "checked"]) {
                            for (k = 0, l = d[f[i]].children_d.length; l > k; k++) d[d[f[i]].children_d[k]].state[o ? "selected" : "checked"] = !0;
                            this._data[o ? "core" : "checkbox"].selected = this._data[o ? "core" : "checkbox"].selected.concat(d[f[i]].children_d)
                        }
                        if (-1 !== n.indexOf("up")) {
                            for (i = 0, j = e.children_d.length; j > i; i++) d[e.children_d[i]].children.length || g.push(d[e.children_d[i]].parent);
                            for (g = a.vakata.array_unique(g), k = 0, l = g.length; l > k; k++) {
                                e = d[g[k]];
                                while (e && "#" !== e.id) {
                                    for (h = 0, i = 0, j = e.children.length; j > i; i++) h += d[e.children[i]].state[o ? "selected" : "checked"];
                                    if (h !== j) break;
                                    e.state[o ? "selected" : "checked"] = !0, this._data[o ? "core" : "checkbox"].selected.push(e.id), m = this.get_node(e, !0), m && m.length && m.attr("aria-selected", !0).children(".jstree-anchor").addClass(o ? "jstree-clicked" : "jstree-checked"), e = this.get_node(e.parent)
                                }
                            }
                        }
                        this._data[o ? "core" : "checkbox"].selected = a.vakata.array_unique(this._data[o ? "core" : "checkbox"].selected)
                    }, this)).on(this.settings.checkbox.tie_selection ? "select_node.jstree" : "check_node.jstree", a.proxy(function (b, c) {
                        var d = c.node, e = this._model.data, f = this.get_node(d.parent), g = this.get_node(d, !0), h,
                            i, j, k, l = this.settings.checkbox.cascade, m = this.settings.checkbox.tie_selection;
                        if (-1 !== l.indexOf("down")) for (this._data[m ? "core" : "checkbox"].selected = a.vakata.array_unique(this._data[m ? "core" : "checkbox"].selected.concat(d.children_d)), h = 0, i = d.children_d.length; i > h; h++) k = e[d.children_d[h]], k.state[m ? "selected" : "checked"] = !0, k && k.original && k.original.state && k.original.state.undetermined && (k.original.state.undetermined = !1);
                        if (-1 !== l.indexOf("up")) while (f && "#" !== f.id) {
                            for (j = 0, h = 0, i = f.children.length; i > h; h++) j += e[f.children[h]].state[m ? "selected" : "checked"];
                            if (j !== i) break;
                            f.state[m ? "selected" : "checked"] = !0, this._data[m ? "core" : "checkbox"].selected.push(f.id), k = this.get_node(f, !0), k && k.length && k.attr("aria-selected", !0).children(".jstree-anchor").addClass(m ? "jstree-clicked" : "jstree-checked"), f = this.get_node(f.parent)
                        }
                        -1 !== l.indexOf("down") && g.length && g.find(".jstree-anchor").addClass(m ? "jstree-clicked" : "jstree-checked").parent().attr("aria-selected", !0)
                    }, this)).on(this.settings.checkbox.tie_selection ? "deselect_all.jstree" : "uncheck_all.jstree", a.proxy(function (a, b) {
                        var c = this.get_node("#"), d = this._model.data, e, f, g;
                        for (e = 0, f = c.children_d.length; f > e; e++) g = d[c.children_d[e]], g && g.original && g.original.state && g.original.state.undetermined && (g.original.state.undetermined = !1)
                    }, this)).on(this.settings.checkbox.tie_selection ? "deselect_node.jstree" : "uncheck_node.jstree", a.proxy(function (b, c) {
                        var d = c.node, e = this.get_node(d, !0), f, g, h, i = this.settings.checkbox.cascade,
                            j = this.settings.checkbox.tie_selection;
                        if (d && d.original && d.original.state && d.original.state.undetermined && (d.original.state.undetermined = !1), -1 !== i.indexOf("down")) for (f = 0, g = d.children_d.length; g > f; f++) h = this._model.data[d.children_d[f]], h.state[j ? "selected" : "checked"] = !1, h && h.original && h.original.state && h.original.state.undetermined && (h.original.state.undetermined = !1);
                        if (-1 !== i.indexOf("up")) for (f = 0, g = d.parents.length; g > f; f++) h = this._model.data[d.parents[f]], h.state[j ? "selected" : "checked"] = !1, h && h.original && h.original.state && h.original.state.undetermined && (h.original.state.undetermined = !1), h = this.get_node(d.parents[f], !0), h && h.length && h.attr("aria-selected", !1).children(".jstree-anchor").removeClass(j ? "jstree-clicked" : "jstree-checked");
                        for (h = [], f = 0, g = this._data[j ? "core" : "checkbox"].selected.length; g > f; f++) -1 !== i.indexOf("down") && -1 !== a.inArray(this._data[j ? "core" : "checkbox"].selected[f], d.children_d) || -1 !== i.indexOf("up") && -1 !== a.inArray(this._data[j ? "core" : "checkbox"].selected[f], d.parents) || h.push(this._data[j ? "core" : "checkbox"].selected[f]);
                        this._data[j ? "core" : "checkbox"].selected = a.vakata.array_unique(h), -1 !== i.indexOf("down") && e.length && e.find(".jstree-anchor").removeClass(j ? "jstree-clicked" : "jstree-checked").parent().attr("aria-selected", !1)
                    }, this)), -1 !== this.settings.checkbox.cascade.indexOf("up") && this.element.on("delete_node.jstree", a.proxy(function (a, b) {
                        var c = this.get_node(b.parent), d = this._model.data, e, f, g, h,
                            i = this.settings.checkbox.tie_selection;
                        while (c && "#" !== c.id) {
                            for (g = 0, e = 0, f = c.children.length; f > e; e++) g += d[c.children[e]].state[i ? "selected" : "checked"];
                            if (g !== f) break;
                            c.state[i ? "selected" : "checked"] = !0, this._data[i ? "core" : "checkbox"].selected.push(c.id), h = this.get_node(c, !0), h && h.length && h.attr("aria-selected", !0).children(".jstree-anchor").addClass(i ? "jstree-clicked" : "jstree-checked"), c = this.get_node(c.parent)
                        }
                    }, this)).on("move_node.jstree", a.proxy(function (b, c) {
                        var d = c.is_multi, e = c.old_parent, f = this.get_node(c.parent), g = this._model.data, h, i,
                            j, k, l, m = this.settings.checkbox.tie_selection;
                        if (!d) {
                            h = this.get_node(e);
                            while (h && "#" !== h.id) {
                                for (i = 0, j = 0, k = h.children.length; k > j; j++) i += g[h.children[j]].state[m ? "selected" : "checked"];
                                if (i !== k) break;
                                h.state[m ? "selected" : "checked"] = !0, this._data[m ? "core" : "checkbox"].selected.push(h.id), l = this.get_node(h, !0), l && l.length && l.attr("aria-selected", !0).children(".jstree-anchor").addClass(m ? "jstree-clicked" : "jstree-checked"), h = this.get_node(h.parent)
                            }
                        }
                        h = f;
                        while (h && "#" !== h.id) {
                            for (i = 0, j = 0, k = h.children.length; k > j; j++) i += g[h.children[j]].state[m ? "selected" : "checked"];
                            if (i === k) h.state[m ? "selected" : "checked"] || (h.state[m ? "selected" : "checked"] = !0, this._data[m ? "core" : "checkbox"].selected.push(h.id), l = this.get_node(h, !0), l && l.length && l.attr("aria-selected", !0).children(".jstree-anchor").addClass(m ? "jstree-clicked" : "jstree-checked")); else {
                                if (!h.state[m ? "selected" : "checked"]) break;
                                h.state[m ? "selected" : "checked"] = !1, this._data[m ? "core" : "checkbox"].selected = a.vakata.array_remove_item(this._data[m ? "core" : "checkbox"].selected, h.id), l = this.get_node(h, !0), l && l.length && l.attr("aria-selected", !1).children(".jstree-anchor").removeClass(m ? "jstree-clicked" : "jstree-checked")
                            }
                            h = this.get_node(h.parent)
                        }
                    }, this))
                }, this._undetermined = function () {
                    var b, c, d = this._model.data, e = this.settings.checkbox.tie_selection,
                        f = this._data[e ? "core" : "checkbox"].selected, g = [], h = this;
                    for (b = 0, c = f.length; c > b; b++) d[f[b]] && d[f[b]].parents && (g = g.concat(d[f[b]].parents));
                    for (this.element.find(".jstree-closed").not(":has(.jstree-children)").each(function () {
                        var a = h.get_node(this), e;
                        if (a.state.loaded) for (b = 0, c = a.children_d.length; c > b; b++) e = d[a.children_d[b]], !e.state.loaded && e.original && e.original.state && e.original.state.undetermined && e.original.state.undetermined === !0 && (g.push(e.id), g = g.concat(e.parents)); else a.original && a.original.state && a.original.state.undetermined && a.original.state.undetermined === !0 && (g.push(a.id), g = g.concat(a.parents))
                    }), g = a.vakata.array_unique(g), g = a.vakata.array_remove_item(g, "#"), this.element.find(".jstree-undetermined").removeClass("jstree-undetermined"), b = 0, c = g.length; c > b; b++) d[g[b]].state[e ? "selected" : "checked"] || (f = this.get_node(g[b], !0), f && f.length && f.children(".jstree-anchor").children(".jstree-checkbox").addClass("jstree-undetermined"))
                }, this.redraw_node = function (b, d, e, f) {
                    if (b = c.redraw_node.apply(this, arguments)) {
                        var g, h, i = null;
                        for (g = 0, h = b.childNodes.length; h > g; g++) if (b.childNodes[g] && b.childNodes[g].className && -1 !== b.childNodes[g].className.indexOf("jstree-anchor")) {
                            i = b.childNodes[g];
                            break
                        }
                        i && (!this.settings.checkbox.tie_selection && this._model.data[b.id].state.checked && (i.className += " jstree-checked"), i.insertBefore(m.cloneNode(!1), i.childNodes[0]))
                    }
                    return e || -1 === this.settings.checkbox.cascade.indexOf("undetermined") || (this._data.checkbox.uto && clearTimeout(this._data.checkbox.uto), this._data.checkbox.uto = setTimeout(a.proxy(this._undetermined, this), 50)), b
                }, this.show_checkboxes = function () {
                    this._data.core.themes.checkboxes = !0, this.get_container_ul().removeClass("jstree-no-checkboxes")
                }, this.hide_checkboxes = function () {
                    this._data.core.themes.checkboxes = !1, this.get_container_ul().addClass("jstree-no-checkboxes")
                }, this.toggle_checkboxes = function () {
                    this._data.core.themes.checkboxes ? this.hide_checkboxes() : this.show_checkboxes()
                }, this.is_undetermined = function (b) {
                    b = this.get_node(b);
                    var c = this.settings.checkbox.cascade, d, e, f = this.settings.checkbox.tie_selection,
                        g = this._data[f ? "core" : "checkbox"].selected, h = this._model.data;
                    if (!b || b.state[f ? "selected" : "checked"] === !0 || -1 === c.indexOf("undetermined") || -1 === c.indexOf("down") && -1 === c.indexOf("up")) return !1;
                    if (!b.state.loaded && b.original.state.undetermined === !0) return !0;
                    for (d = 0, e = b.children_d.length; e > d; d++) if (-1 !== a.inArray(b.children_d[d], g) || !h[b.children_d[d]].state.loaded && h[b.children_d[d]].original.state.undetermined) return !0;
                    return !1
                }, this.activate_node = function (b, d) {
                    return this.settings.checkbox.tie_selection && (this.settings.checkbox.whole_node || a(d.target).hasClass("jstree-checkbox")) && (d.ctrlKey = !0), this.settings.checkbox.tie_selection || !this.settings.checkbox.whole_node && !a(d.target).hasClass("jstree-checkbox") ? c.activate_node.call(this, b, d) : this.is_disabled(b) ? !1 : (this.is_checked(b) ? this.uncheck_node(b, d) : this.check_node(b, d), void this.trigger("activate_node", {node: this.get_node(b)}))
                }, this.check_node = function (b, c) {
                    if (this.settings.checkbox.tie_selection) return this.select_node(b, !1, !0, c);
                    var d, e, f, g;
                    if (a.isArray(b)) {
                        for (b = b.slice(), e = 0, f = b.length; f > e; e++) this.check_node(b[e], c);
                        return !0
                    }
                    return b = this.get_node(b), b && "#" !== b.id ? (d = this.get_node(b, !0), void (b.state.checked || (b.state.checked = !0, this._data.checkbox.selected.push(b.id), d && d.length && d.children(".jstree-anchor").addClass("jstree-checked"), this.trigger("check_node", {
                        node: b,
                        selected: this._data.checkbox.selected,
                        event: c
                    })))) : !1
                }, this.uncheck_node = function (b, c) {
                    if (this.settings.checkbox.tie_selection) return this.deselect_node(b, !1, c);
                    var d, e, f;
                    if (a.isArray(b)) {
                        for (b = b.slice(), d = 0, e = b.length; e > d; d++) this.uncheck_node(b[d], c);
                        return !0
                    }
                    return b = this.get_node(b), b && "#" !== b.id ? (f = this.get_node(b, !0), void (b.state.checked && (b.state.checked = !1, this._data.checkbox.selected = a.vakata.array_remove_item(this._data.checkbox.selected, b.id), f.length && f.children(".jstree-anchor").removeClass("jstree-checked"), this.trigger("uncheck_node", {
                        node: b,
                        selected: this._data.checkbox.selected,
                        event: c
                    })))) : !1
                }, this.check_all = function () {
                    if (this.settings.checkbox.tie_selection) return this.select_all();
                    var a = this._data.checkbox.selected.concat([]), b, c;
                    for (this._data.checkbox.selected = this._model.data["#"].children_d.concat(), b = 0, c = this._data.checkbox.selected.length; c > b; b++) this._model.data[this._data.checkbox.selected[b]] && (this._model.data[this._data.checkbox.selected[b]].state.checked = !0);
                    this.redraw(!0), this.trigger("check_all", {selected: this._data.checkbox.selected})
                }, this.uncheck_all = function () {
                    if (this.settings.checkbox.tie_selection) return this.deselect_all();
                    var a = this._data.checkbox.selected.concat([]), b, c;
                    for (b = 0, c = this._data.checkbox.selected.length; c > b; b++) this._model.data[this._data.checkbox.selected[b]] && (this._model.data[this._data.checkbox.selected[b]].state.checked = !1);
                    this._data.checkbox.selected = [], this.element.find(".jstree-checked").removeClass("jstree-checked"), this.trigger("uncheck_all", {
                        selected: this._data.checkbox.selected,
                        node: a
                    })
                }, this.is_checked = function (a) {
                    return this.settings.checkbox.tie_selection ? this.is_selected(a) : (a = this.get_node(a), a && "#" !== a.id ? a.state.checked : !1)
                }, this.get_checked = function (b) {
                    return this.settings.checkbox.tie_selection ? this.get_selected(b) : b ? a.map(this._data.checkbox.selected, a.proxy(function (a) {
                        return this.get_node(a)
                    }, this)) : this._data.checkbox.selected
                }, this.get_top_checked = function (b) {
                    if (this.settings.checkbox.tie_selection) return this.get_top_selected(b);
                    var c = this.get_checked(!0), d = {}, e, f, g, h;
                    for (e = 0, f = c.length; f > e; e++) d[c[e].id] = c[e];
                    for (e = 0, f = c.length; f > e; e++) for (g = 0, h = c[e].children_d.length; h > g; g++) d[c[e].children_d[g]] && delete d[c[e].children_d[g]];
                    c = [];
                    for (e in d) d.hasOwnProperty(e) && c.push(e);
                    return b ? a.map(c, a.proxy(function (a) {
                        return this.get_node(a)
                    }, this)) : c
                }, this.get_bottom_checked = function (b) {
                    if (this.settings.checkbox.tie_selection) return this.get_bottom_selected(b);
                    var c = this.get_checked(!0), d = [], e, f;
                    for (e = 0, f = c.length; f > e; e++) c[e].children.length || d.push(c[e].id);
                    return b ? a.map(d, a.proxy(function (a) {
                        return this.get_node(a)
                    }, this)) : d
                }, this.load_node = function (b, d) {
                    var e, f, g, h, i, j;
                    if (!a.isArray(b) && !this.settings.checkbox.tie_selection && (j = this.get_node(b), j && j.state.loaded)) for (e = 0, f = j.children_d.length; f > e; e++) this._model.data[j.children_d[e]].state.checked && (i = !0, this._data.checkbox.selected = a.vakata.array_remove_item(this._data.checkbox.selected, j.children_d[e]));
                    return c.load_node.apply(this, arguments)
                }, this.get_state = function () {
                    var a = c.get_state.apply(this, arguments);
                    return this.settings.checkbox.tie_selection ? a : (a.checkbox = this._data.checkbox.selected.slice(), a)
                }, this.set_state = function (b, d) {
                    var e = c.set_state.apply(this, arguments);
                    if (e && b.checkbox) {
                        if (!this.settings.checkbox.tie_selection) {
                            this.uncheck_all();
                            var f = this;
                            a.each(b.checkbox, function (a, b) {
                                f.check_node(b)
                            })
                        }
                        return delete b.checkbox, !1
                    }
                    return e
                }
            };
            var n = null, o, p;
            a.jstree.defaults.contextmenu = {
                select_node: !0, show_at_node: !0, items: function (b, c) {
                    return {
                        create: {
                            separator_before: !1,
                            separator_after: !0,
                            _disabled: !1,
                            label: "Create",
                            action: function (b) {
                                var c = a.jstree.reference(b.reference), d = c.get_node(b.reference);
                                c.create_node(d, {}, "last", function (a) {
                                    setTimeout(function () {
                                        c.edit(a)
                                    }, 0)
                                })
                            }
                        },
                        rename: {
                            separator_before: !1,
                            separator_after: !1,
                            _disabled: !1,
                            label: "Rename",
                            action: function (b) {
                                var c = a.jstree.reference(b.reference), d = c.get_node(b.reference);
                                c.edit(d)
                            }
                        },
                        remove: {
                            separator_before: !1,
                            icon: !1,
                            separator_after: !1,
                            _disabled: !1,
                            label: "Delete",
                            action: function (b) {
                                var c = a.jstree.reference(b.reference), d = c.get_node(b.reference);
                                c.delete_node(c.is_selected(d) ? c.get_selected() : d)
                            }
                        },
                        ccp: {
                            separator_before: !0,
                            icon: !1,
                            separator_after: !1,
                            label: "Edit",
                            action: !1,
                            submenu: {
                                cut: {
                                    separator_before: !1,
                                    separator_after: !1,
                                    label: "Cut",
                                    action: function (b) {
                                        var c = a.jstree.reference(b.reference), d = c.get_node(b.reference);
                                        c.cut(c.is_selected(d) ? c.get_selected() : d)
                                    }
                                },
                                copy: {
                                    separator_before: !1,
                                    icon: !1,
                                    separator_after: !1,
                                    label: "Copy",
                                    action: function (b) {
                                        var c = a.jstree.reference(b.reference), d = c.get_node(b.reference);
                                        c.copy(c.is_selected(d) ? c.get_selected() : d)
                                    }
                                },
                                paste: {
                                    separator_before: !1, icon: !1, _disabled: function (b) {
                                        return !a.jstree.reference(b.reference).can_paste()
                                    }, separator_after: !1, label: "Paste", action: function (b) {
                                        var c = a.jstree.reference(b.reference), d = c.get_node(b.reference);
                                        c.paste(d)
                                    }
                                }
                            }
                        }
                    }
                }
            }, a.jstree.plugins.contextmenu = function (c, d) {
                this.bind = function () {
                    d.bind.call(this);
                    var b = 0;
                    this.element.on("contextmenu.jstree", ".jstree-anchor", a.proxy(function (a, c) {
                        a.preventDefault(), b = a.ctrlKey ? +new Date : 0, (c || n) && (b = +new Date + 1e4), n && clearTimeout(n), this.is_loading(a.currentTarget) || this.show_contextmenu(a.currentTarget, a.pageX, a.pageY, a)
                    }, this)).on("click.jstree", ".jstree-anchor", a.proxy(function (c) {
                        this._data.contextmenu.visible && (!b || +new Date - b > 250) && a.vakata.context.hide(), b = 0
                    }, this)).on("touchstart.jstree", ".jstree-anchor", function (b) {
                        b.originalEvent && b.originalEvent.changedTouches && b.originalEvent.changedTouches[0] && (o = b.pageX, p = b.pageY, n = setTimeout(function () {
                            a(b.currentTarget).trigger("contextmenu", !0)
                        }, 750))
                    }), a(document).on("context_hide.vakata.jstree", a.proxy(function () {
                        this._data.contextmenu.visible = !1
                    }, this))
                }, this.teardown = function () {
                    this._data.contextmenu.visible && a.vakata.context.hide(), d.teardown.call(this)
                }, this.show_contextmenu = function (c, d, e, f) {
                    if (c = this.get_node(c), !c || "#" === c.id) return !1;
                    var g = this.settings.contextmenu, h = this.get_node(c, !0), i = h.children(".jstree-anchor"),
                        j = !1, k = !1;
                    (g.show_at_node || d === b || e === b) && (j = i.offset(), d = j.left, e = j.top + this._data.core.li_height), this.settings.contextmenu.select_node && !this.is_selected(c) && this.activate_node(c, f), k = g.items, a.isFunction(k) && (k = k.call(this, c, a.proxy(function (a) {
                        this._show_contextmenu(c, d, e, a)
                    }, this))), a.isPlainObject(k) && this._show_contextmenu(c, d, e, k)
                }, this._show_contextmenu = function (b, c, d, e) {
                    var f = this.get_node(b, !0), g = f.children(".jstree-anchor");
                    a(document).one("context_show.vakata.jstree", a.proxy(function (b, c) {
                        var d = "jstree-contextmenu jstree-" + this.get_theme() + "-contextmenu";
                        a(c.element).addClass(d)
                    }, this)), this._data.contextmenu.visible = !0, a.vakata.context.show(g, {
                        x: c,
                        y: d
                    }, e), this.trigger("show_contextmenu", {node: b, x: c, y: d})
                }
            }, a(function () {
                a(document).on("touchmove.vakata.jstree", function (a) {
                    n && a.originalEvent && a.originalEvent.changedTouches && a.originalEvent.changedTouches[0] && (Math.abs(o - a.pageX) > 50 || Math.abs(p - a.pageY) > 50) && clearTimeout(n)
                }).on("touchend.vakata.jstree", function (a) {
                    n && clearTimeout(n)
                })
            }), function (a) {
                var b = !1,
                    c = {element: !1, reference: !1, position_x: 0, position_y: 0, items: [], html: "", is_visible: !1};
                a.vakata.context = {
                    settings: {hide_onmouseleave: 0, icons: !0}, _trigger: function (b) {
                        a(document).triggerHandler("context_" + b + ".vakata", {
                            reference: c.reference,
                            element: c.element,
                            position: {x: c.position_x, y: c.position_y}
                        })
                    }, _execute: function (b) {
                        return b = c.items[b], b && (!b._disabled || a.isFunction(b._disabled) && !b._disabled({
                            item: b,
                            reference: c.reference,
                            element: c.element
                        })) && b.action ? b.action.call(null, {
                            item: b,
                            reference: c.reference,
                            element: c.element,
                            position: {x: c.position_x, y: c.position_y}
                        }) : !1
                    }, _parse: function (b, d) {
                        if (!b) return !1;
                        d || (c.html = "", c.items = []);
                        var e = "", f = !1, g;
                        return d && (e += "<ul>"), a.each(b, function (b, d) {
                            return d ? (c.items.push(d), !f && d.separator_before && (e += "<li class='vakata-context-separator'><a href='#' " + (a.vakata.context.settings.icons ? "" : 'style="margin-left:0px;"') + ">&#160;</a></li>"), f = !1, e += "<li class='" + (d._class || "") + (d._disabled === !0 || a.isFunction(d._disabled) && d._disabled({
                                item: d,
                                reference: c.reference,
                                element: c.element
                            }) ? " vakata-contextmenu-disabled " : "") + "' " + (d.shortcut ? " data-shortcut='" + d.shortcut + "' " : "") + ">", e += "<a href='#' rel='" + (c.items.length - 1) + "'>", a.vakata.context.settings.icons && (e += "<i ", d.icon && (e += -1 !== d.icon.indexOf("/") || -1 !== d.icon.indexOf(".") ? " style='background:url(\"" + d.icon + "\") center center no-repeat' " : " class='" + d.icon + "' "), e += "></i><span class='vakata-contextmenu-sep'>&#160;</span>"), e += (a.isFunction(d.label) ? d.label({
                                item: b,
                                reference: c.reference,
                                element: c.element
                            }) : d.label) + (d.shortcut ? ' <span class="vakata-contextmenu-shortcut vakata-contextmenu-shortcut-' + d.shortcut + '">' + (d.shortcut_label || "") + "</span>" : "") + "</a>", d.submenu && (g = a.vakata.context._parse(d.submenu, !0), g && (e += g)), e += "</li>", void (d.separator_after && (e += "<li class='vakata-context-separator'><a href='#' " + (a.vakata.context.settings.icons ? "" : 'style="margin-left:0px;"') + ">&#160;</a></li>", f = !0))) : !0
                        }), e = e.replace(/<li class\='vakata-context-separator'\><\/li\>$/, ""), d && (e += "</ul>"), d || (c.html = e, a.vakata.context._trigger("parse")), e.length > 10 ? e : !1
                    }, _show_submenu: function (c) {
                        if (c = a(c), c.length && c.children("ul").length) {
                            var d = c.children("ul"), e = c.offset().left + c.outerWidth(), f = c.offset().top,
                                g = d.width(), h = d.height(), i = a(window).width() + a(window).scrollLeft(),
                                j = a(window).height() + a(window).scrollTop();
                            b ? c[e - (g + 10 + c.outerWidth()) < 0 ? "addClass" : "removeClass"]("vakata-context-left") : c[e + g + 10 > i ? "addClass" : "removeClass"]("vakata-context-right"), f + h + 10 > j && d.css("bottom", "-1px"), d.show()
                        }
                    }, show: function (d, e, f) {
                        var g, h, i, j, k, l, m, n, o = !0;
                        switch (c.element && c.element.length && c.element.width(""), o) {
                            case!e && !d:
                                return !1;
                            case!!e && !!d:
                                c.reference = d, c.position_x = e.x, c.position_y = e.y;
                                break;
                            case!e && !!d:
                                c.reference = d, g = d.offset(), c.position_x = g.left + d.outerHeight(), c.position_y = g.top;
                                break;
                            case!!e && !d:
                                c.position_x = e.x, c.position_y = e.y
                        }
                        d && !f && a(d).data("vakata_contextmenu") && (f = a(d).data("vakata_contextmenu")), a.vakata.context._parse(f) && c.element.html(c.html), c.items.length && (c.element.appendTo("body"), h = c.element, i = c.position_x, j = c.position_y, k = h.width(), l = h.height(), m = a(window).width() + a(window).scrollLeft(), n = a(window).height() + a(window).scrollTop(), b && (i -= h.outerWidth() - a(d).outerWidth(), i < a(window).scrollLeft() + 20 && (i = a(window).scrollLeft() + 20)), i + k + 20 > m && (i = m - (k + 20)), j + l + 20 > n && (j = n - (l + 20)), c.element.css({
                            left: i,
                            top: j
                        }).show().find("a").first().focus().parent().addClass("vakata-context-hover"), c.is_visible = !0, a.vakata.context._trigger("show"))
                    }, hide: function () {
                        c.is_visible && (c.element.hide().find("ul").hide().end().find(":focus").blur().end().detach(), c.is_visible = !1, a.vakata.context._trigger("hide"))
                    }
                }, a(function () {
                    b = "rtl" === a("body").css("direction");
                    var d = !1;
                    c.element = a("<ul class='vakata-context'></ul>"), c.element.on("mouseenter", "li", function (b) {
                        b.stopImmediatePropagation(), a.contains(this, b.relatedTarget) || (d && clearTimeout(d), c.element.find(".vakata-context-hover").removeClass("vakata-context-hover").end(), a(this).siblings().find("ul").hide().end().end().parentsUntil(".vakata-context", "li").addBack().addClass("vakata-context-hover"), a.vakata.context._show_submenu(this))
                    }).on("mouseleave", "li", function (b) {
                        a.contains(this, b.relatedTarget) || a(this).find(".vakata-context-hover").addBack().removeClass("vakata-context-hover")
                    }).on("mouseleave", function (b) {
                        a(this).find(".vakata-context-hover").removeClass("vakata-context-hover"), a.vakata.context.settings.hide_onmouseleave && (d = setTimeout(function (b) {
                            return function () {
                                a.vakata.context.hide()
                            }
                        }(this), a.vakata.context.settings.hide_onmouseleave))
                    }).on("click", "a", function (b) {
                        b.preventDefault(), a(this).blur().parent().hasClass("vakata-context-disabled") || a.vakata.context._execute(a(this).attr("rel")) === !1 || a.vakata.context.hide()
                    }).on("keydown", "a", function (b) {
                        var d = null;
                        switch (b.which) {
                            case 13:
                            case 32:
                                b.type = "mouseup", b.preventDefault(), a(b.currentTarget).trigger(b);
                                break;
                            case 37:
                                c.is_visible && (c.element.find(".vakata-context-hover").last().closest("li").first().find("ul").hide().find(".vakata-context-hover").removeClass("vakata-context-hover").end().end().children("a").focus(), b.stopImmediatePropagation(), b.preventDefault());
                                break;
                            case 38:
                                c.is_visible && (d = c.element.find("ul:visible").addBack().last().children(".vakata-context-hover").removeClass("vakata-context-hover").prevAll("li:not(.vakata-context-separator)").first(), d.length || (d = c.element.find("ul:visible").addBack().last().children("li:not(.vakata-context-separator)").last()), d.addClass("vakata-context-hover").children("a").focus(), b.stopImmediatePropagation(), b.preventDefault());
                                break;
                            case 39:
                                c.is_visible && (c.element.find(".vakata-context-hover").last().children("ul").show().children("li:not(.vakata-context-separator)").removeClass("vakata-context-hover").first().addClass("vakata-context-hover").children("a").focus(), b.stopImmediatePropagation(), b.preventDefault());
                                break;
                            case 40:
                                c.is_visible && (d = c.element.find("ul:visible").addBack().last().children(".vakata-context-hover").removeClass("vakata-context-hover").nextAll("li:not(.vakata-context-separator)").first(), d.length || (d = c.element.find("ul:visible").addBack().last().children("li:not(.vakata-context-separator)").first()), d.addClass("vakata-context-hover").children("a").focus(), b.stopImmediatePropagation(), b.preventDefault());
                                break;
                            case 27:
                                a.vakata.context.hide(), b.preventDefault()
                        }
                    }).on("keydown", function (a) {
                        a.preventDefault();
                        var b = c.element.find(".vakata-contextmenu-shortcut-" + a.which).parent();
                        b.parent().not(".vakata-context-disabled") && b.click()
                    }), a(document).on("mousedown.vakata.jstree", function (b) {
                        c.is_visible && !a.contains(c.element[0], b.target) && a.vakata.context.hide()
                    }).on("context_show.vakata.jstree", function (a, d) {
                        c.element.find("li:has(ul)").children("a").addClass("vakata-context-parent"), b && c.element.addClass("vakata-context-rtl").css("direction", "rtl"), c.element.find("ul").hide().end()
                    })
                })
            }(a), a.jstree.defaults.dnd = {
                copy: !0,
                open_timeout: 500,
                is_draggable: !0,
                check_while_dragging: !0,
                always_copy: !1,
                inside_pos: 0,
                drag_selection: !0,
                touch: !0
            }, a.jstree.plugins.dnd = function (b, c) {
                this.bind = function () {
                    c.bind.call(this), this.element.on("mousedown.jstree touchstart.jstree", ".jstree-anchor", a.proxy(function (b) {
                        if ("touchstart" === b.type && (!this.settings.dnd.touch || "selected" === this.settings.dnd.touch && !a(b.currentTarget).hasClass("jstree-clicked"))) return !0;
                        var c = this.get_node(b.target),
                            d = this.is_selected(c) && this.settings.drag_selection ? this.get_selected().length : 1,
                            e = d > 1 ? d + " " + this.get_string("nodes") : this.get_text(b.currentTarget);
                        return this.settings.core.force_text && (e = a("<div />").text(e).html()), c && c.id && "#" !== c.id && (1 === b.which || "touchstart" === b.type) && (this.settings.dnd.is_draggable === !0 || a.isFunction(this.settings.dnd.is_draggable) && this.settings.dnd.is_draggable.call(this, d > 1 ? this.get_selected(!0) : [c])) ? (this.element.trigger("mousedown.jstree"), a.vakata.dnd.start(b, {
                            jstree: !0,
                            origin: this,
                            obj: this.get_node(c, !0),
                            nodes: d > 1 ? this.get_selected() : [c.id]
                        }, '<div id="jstree-dnd" class="jstree-' + this.get_theme() + " jstree-" + this.get_theme() + "-" + this.get_theme_variant() + " " + (this.settings.core.themes.responsive ? " jstree-dnd-responsive" : "") + '"><i class="jstree-icon jstree-er"></i>' + e + '<ins class="jstree-copy" style="display:none;">+</ins></div>')) : void 0
                    }, this))
                }
            }, a(function () {
                var b = !1, c = !1, d = !1, e = a('<div id="jstree-marker">&#160;</div>').hide();
                a(document).on("dnd_start.vakata.jstree", function (a, c) {
                    b = !1, c && c.data && c.data.jstree && e.appendTo("body")
                }).on("dnd_move.vakata.jstree", function (f, g) {
                    if (d && clearTimeout(d), g && g.data && g.data.jstree && (!g.event.target.id || "jstree-marker" !== g.event.target.id)) {
                        var h = a.jstree.reference(g.event.target), i = !1, j = !1, k = !1, l, m, n, o, p, q, r, s, t,
                            u, v, w, x, y;
                        if (h && h._data && h._data.dnd) if (e.attr("class", "jstree-" + h.get_theme() + (h.settings.core.themes.responsive ? " jstree-dnd-responsive" : "")), g.helper.children().attr("class", "jstree-" + h.get_theme() + " jstree-" + h.get_theme() + "-" + h.get_theme_variant() + " " + (h.settings.core.themes.responsive ? " jstree-dnd-responsive" : "")).find(".jstree-copy").first()[g.data.origin && (g.data.origin.settings.dnd.always_copy || g.data.origin.settings.dnd.copy && (g.event.metaKey || g.event.ctrlKey)) ? "show" : "hide"](), g.event.target !== h.element[0] && g.event.target !== h.get_container_ul()[0] || 0 !== h.get_container_ul().children().length) {
                            if (i = a(g.event.target).closest(".jstree-anchor"), i && i.length && i.parent().is(".jstree-closed, .jstree-open, .jstree-leaf") && (j = i.offset(), k = g.event.pageY - j.top, n = i.height(), q = n / 3 > k ? ["b", "i", "a"] : k > n - n / 3 ? ["a", "i", "b"] : k > n / 2 ? ["i", "a", "b"] : ["i", "b", "a"], a.each(q, function (f, k) {
                                switch (k) {
                                    case"b":
                                        l = j.left - 6, m = j.top, o = h.get_parent(i), p = i.parent().index();
                                        break;
                                    case"i":
                                        x = h.settings.dnd.inside_pos, y = h.get_node(i.parent()), l = j.left - 2, m = j.top + n / 2 + 1, o = y.id, p = "first" === x ? 0 : "last" === x ? y.children.length : Math.min(x, y.children.length);
                                        break;
                                    case"a":
                                        l = j.left - 6, m = j.top + n, o = h.get_parent(i), p = i.parent().index() + 1
                                }
                                for (r = !0, s = 0, t = g.data.nodes.length; t > s; s++) if (u = g.data.origin && (g.data.origin.settings.dnd.always_copy || g.data.origin.settings.dnd.copy && (g.event.metaKey || g.event.ctrlKey)) ? "copy_node" : "move_node", v = p, "move_node" === u && "a" === k && g.data.origin && g.data.origin === h && o === h.get_parent(g.data.nodes[s]) && (w = h.get_node(o), v > a.inArray(g.data.nodes[s], w.children) && (v -= 1)), r = r && (h && h.settings && h.settings.dnd && h.settings.dnd.check_while_dragging === !1 || h.check(u, g.data.origin && g.data.origin !== h ? g.data.origin.get_node(g.data.nodes[s]) : g.data.nodes[s], o, v, {
                                    dnd: !0,
                                    ref: h.get_node(i.parent()),
                                    pos: k,
                                    is_multi: g.data.origin && g.data.origin !== h,
                                    is_foreign: !g.data.origin
                                })), !r) {
                                    h && h.last_error && (c = h.last_error());
                                    break
                                }
                                return "i" === k && i.parent().is(".jstree-closed") && h.settings.dnd.open_timeout && (d = setTimeout(function (a, b) {
                                    return function () {
                                        a.open_node(b)
                                    }
                                }(h, i), h.settings.dnd.open_timeout)), r ? (b = {
                                    ins: h,
                                    par: o,
                                    pos: "i" !== k || "last" !== x || 0 !== p || h.is_loaded(y) ? p : "last"
                                }, e.css({
                                    left: l + "px",
                                    top: m + "px"
                                }).show(), g.helper.find(".jstree-icon").first().removeClass("jstree-er").addClass("jstree-ok"), c = {}, q = !0, !1) : void 0
                            }), q === !0)) return
                        } else {
                            for (r = !0, s = 0, t = g.data.nodes.length; t > s; s++) if (r = r && h.check(g.data.origin && (g.data.origin.settings.dnd.always_copy || g.data.origin.settings.dnd.copy && (g.event.metaKey || g.event.ctrlKey)) ? "copy_node" : "move_node", g.data.origin && g.data.origin !== h ? g.data.origin.get_node(g.data.nodes[s]) : g.data.nodes[s], "#", "last", {
                                dnd: !0,
                                ref: h.get_node("#"),
                                pos: "i",
                                is_multi: g.data.origin && g.data.origin !== h,
                                is_foreign: !g.data.origin
                            }), !r) break;
                            if (r) return b = {
                                ins: h,
                                par: "#",
                                pos: "last"
                            }, e.hide(), void g.helper.find(".jstree-icon").first().removeClass("jstree-er").addClass("jstree-ok")
                        }
                        b = !1, g.helper.find(".jstree-icon").removeClass("jstree-ok").addClass("jstree-er"), e.hide()
                    }
                }).on("dnd_scroll.vakata.jstree", function (a, c) {
                    c && c.data && c.data.jstree && (e.hide(), b = !1, c.helper.find(".jstree-icon").first().removeClass("jstree-ok").addClass("jstree-er"))
                }).on("dnd_stop.vakata.jstree", function (f, g) {
                    if (d && clearTimeout(d), g && g.data && g.data.jstree) {
                        e.hide().detach();
                        var h, i, j = [];
                        if (b) {
                            for (h = 0, i = g.data.nodes.length; i > h; h++) j[h] = g.data.origin ? g.data.origin.get_node(g.data.nodes[h]) : g.data.nodes[h], g.data.origin && (j[h].instance = g.data.origin);
                            for (b.ins[g.data.origin && (g.data.origin.settings.dnd.always_copy || g.data.origin.settings.dnd.copy && (g.event.metaKey || g.event.ctrlKey)) ? "copy_node" : "move_node"](j, b.par, b.pos), h = 0, i = j.length; i > h; h++) j[h].instance && (j[h].instance = null)
                        } else h = a(g.event.target).closest(".jstree"), h.length && c && c.error && "check" === c.error && (h = h.jstree(!0), h && h.settings.core.error.call(this, c))
                    }
                }).on("keyup.jstree keydown.jstree", function (b, c) {
                    c = a.vakata.dnd._get(), c && c.data && c.data.jstree && c.helper.find(".jstree-copy").first()[c.data.origin && (c.data.origin.settings.dnd.always_copy || c.data.origin.settings.dnd.copy && (b.metaKey || b.ctrlKey)) ? "show" : "hide"]()
                })
            }), function (a) {
                var b = {
                    element: !1,
                    target: !1,
                    is_down: !1,
                    is_drag: !1,
                    helper: !1,
                    helper_w: 0,
                    data: !1,
                    init_x: 0,
                    init_y: 0,
                    scroll_l: 0,
                    scroll_t: 0,
                    scroll_e: !1,
                    scroll_i: !1,
                    is_touch: !1
                };
                a.vakata.dnd = {
                    settings: {
                        scroll_speed: 10,
                        scroll_proximity: 20,
                        helper_left: 5,
                        helper_top: 10,
                        threshold: 5,
                        threshold_touch: 50
                    }, _trigger: function (b, c) {
                        var d = a.vakata.dnd._get();
                        d.event = c, a(document).triggerHandler("dnd_" + b + ".vakata", d)
                    }, _get: function () {
                        return {data: b.data, element: b.element, helper: b.helper}
                    }, _clean: function () {
                        b.helper && b.helper.remove(), b.scroll_i && (clearInterval(b.scroll_i), b.scroll_i = !1), b = {
                            element: !1,
                            target: !1,
                            is_down: !1,
                            is_drag: !1,
                            helper: !1,
                            helper_w: 0,
                            data: !1,
                            init_x: 0,
                            init_y: 0,
                            scroll_l: 0,
                            scroll_t: 0,
                            scroll_e: !1,
                            scroll_i: !1,
                            is_touch: !1
                        }, a(document).off("mousemove.vakata.jstree touchmove.vakata.jstree", a.vakata.dnd.drag), a(document).off("mouseup.vakata.jstree touchend.vakata.jstree", a.vakata.dnd.stop)
                    }, _scroll: function (c) {
                        if (!b.scroll_e || !b.scroll_l && !b.scroll_t) return b.scroll_i && (clearInterval(b.scroll_i), b.scroll_i = !1), !1;
                        if (!b.scroll_i) return b.scroll_i = setInterval(a.vakata.dnd._scroll, 100), !1;
                        if (c === !0) return !1;
                        var d = b.scroll_e.scrollTop(), e = b.scroll_e.scrollLeft();
                        b.scroll_e.scrollTop(d + b.scroll_t * a.vakata.dnd.settings.scroll_speed), b.scroll_e.scrollLeft(e + b.scroll_l * a.vakata.dnd.settings.scroll_speed), (d !== b.scroll_e.scrollTop() || e !== b.scroll_e.scrollLeft()) && a.vakata.dnd._trigger("scroll", b.scroll_e)
                    }, start: function (c, d, e) {
                        "touchstart" === c.type && c.originalEvent && c.originalEvent.changedTouches && c.originalEvent.changedTouches[0] && (c.pageX = c.originalEvent.changedTouches[0].pageX, c.pageY = c.originalEvent.changedTouches[0].pageY, c.target = document.elementFromPoint(c.originalEvent.changedTouches[0].pageX - window.pageXOffset, c.originalEvent.changedTouches[0].pageY - window.pageYOffset)), b.is_drag && a.vakata.dnd.stop({});
                        try {
                            c.currentTarget.unselectable = "on", c.currentTarget.onselectstart = function () {
                                return !1
                            }, c.currentTarget.style && (c.currentTarget.style.MozUserSelect = "none")
                        } catch (f) {
                        }
                        return b.init_x = c.pageX, b.init_y = c.pageY, b.data = d, b.is_down = !0, b.element = c.currentTarget, b.target = c.target, b.is_touch = "touchstart" === c.type, e !== !1 && (b.helper = a("<div id='vakata-dnd'></div>").html(e).css({
                            display: "block",
                            margin: "0",
                            padding: "0",
                            position: "absolute",
                            top: "-2000px",
                            lineHeight: "16px",
                            zIndex: "10000"
                        })), a(document).on("mousemove.vakata.jstree touchmove.vakata.jstree", a.vakata.dnd.drag), a(document).on("mouseup.vakata.jstree touchend.vakata.jstree", a.vakata.dnd.stop), !1
                    }, drag: function (c) {
                        if ("touchmove" === c.type && c.originalEvent && c.originalEvent.changedTouches && c.originalEvent.changedTouches[0] && (c.pageX = c.originalEvent.changedTouches[0].pageX, c.pageY = c.originalEvent.changedTouches[0].pageY, c.target = document.elementFromPoint(c.originalEvent.changedTouches[0].pageX - window.pageXOffset, c.originalEvent.changedTouches[0].pageY - window.pageYOffset)), b.is_down) {
                            if (!b.is_drag) {
                                if (!(Math.abs(c.pageX - b.init_x) > (b.is_touch ? a.vakata.dnd.settings.threshold_touch : a.vakata.dnd.settings.threshold) || Math.abs(c.pageY - b.init_y) > (b.is_touch ? a.vakata.dnd.settings.threshold_touch : a.vakata.dnd.settings.threshold))) return;
                                b.helper && (b.helper.appendTo("body"), b.helper_w = b.helper.outerWidth()), b.is_drag = !0, a.vakata.dnd._trigger("start", c)
                            }
                            var d = !1, e = !1, f = !1, g = !1, h = !1, i = !1, j = !1, k = !1, l = !1, m = !1;
                            return b.scroll_t = 0, b.scroll_l = 0, b.scroll_e = !1, a(a(c.target).parentsUntil("body").addBack().get().reverse()).filter(function () {
                                return /^auto|scroll$/.test(a(this).css("overflow")) && (this.scrollHeight > this.offsetHeight || this.scrollWidth > this.offsetWidth)
                            }).each(function () {
                                var d = a(this), e = d.offset();
                                return this.scrollHeight > this.offsetHeight && (e.top + d.height() - c.pageY < a.vakata.dnd.settings.scroll_proximity && (b.scroll_t = 1), c.pageY - e.top < a.vakata.dnd.settings.scroll_proximity && (b.scroll_t = -1)), this.scrollWidth > this.offsetWidth && (e.left + d.width() - c.pageX < a.vakata.dnd.settings.scroll_proximity && (b.scroll_l = 1), c.pageX - e.left < a.vakata.dnd.settings.scroll_proximity && (b.scroll_l = -1)), b.scroll_t || b.scroll_l ? (b.scroll_e = a(this), !1) : void 0
                            }), b.scroll_e || (d = a(document), e = a(window), f = d.height(), g = e.height(), h = d.width(), i = e.width(), j = d.scrollTop(), k = d.scrollLeft(), f > g && c.pageY - j < a.vakata.dnd.settings.scroll_proximity && (b.scroll_t = -1), f > g && g - (c.pageY - j) < a.vakata.dnd.settings.scroll_proximity && (b.scroll_t = 1), h > i && c.pageX - k < a.vakata.dnd.settings.scroll_proximity && (b.scroll_l = -1), h > i && i - (c.pageX - k) < a.vakata.dnd.settings.scroll_proximity && (b.scroll_l = 1), (b.scroll_t || b.scroll_l) && (b.scroll_e = d)), b.scroll_e && a.vakata.dnd._scroll(!0), b.helper && (l = parseInt(c.pageY + a.vakata.dnd.settings.helper_top, 10), m = parseInt(c.pageX + a.vakata.dnd.settings.helper_left, 10), f && l + 25 > f && (l = f - 50), h && m + b.helper_w > h && (m = h - (b.helper_w + 2)), b.helper.css({
                                left: m + "px",
                                top: l + "px"
                            })), a.vakata.dnd._trigger("move", c), !1
                        }
                    }, stop: function (c) {
                        if ("touchend" === c.type && c.originalEvent && c.originalEvent.changedTouches && c.originalEvent.changedTouches[0] && (c.pageX = c.originalEvent.changedTouches[0].pageX, c.pageY = c.originalEvent.changedTouches[0].pageY, c.target = document.elementFromPoint(c.originalEvent.changedTouches[0].pageX - window.pageXOffset, c.originalEvent.changedTouches[0].pageY - window.pageYOffset)), b.is_drag) a.vakata.dnd._trigger("stop", c); else if ("touchend" === c.type && c.target === b.target) {
                            var d = setTimeout(function () {
                                a(c.target).click()
                            }, 100);
                            a(c.target).one("click", function () {
                                d && clearTimeout(d)
                            })
                        }
                        return a.vakata.dnd._clean(), !1
                    }
                }
            }(a), a.jstree.defaults.search = {
                ajax: !1,
                fuzzy: !1,
                case_sensitive: !1,
                show_only_matches: !1,
                close_opened_onclear: !0,
                search_leaves_only: !1,
                search_callback: !1
            }, a.jstree.plugins.search = function (c, d) {
                this.bind = function () {
                    d.bind.call(this), this._data.search.str = "", this._data.search.dom = a(), this._data.search.res = [], this._data.search.opn = [], this._data.search.som = !1, this.element.on("before_open.jstree", a.proxy(function (b, c) {
                        var d, e, f, g = this._data.search.res, h = [], i = a();
                        if (g && g.length && (this._data.search.dom = a(this.element[0].querySelectorAll("#" + a.map(g, function (b) {
                            return -1 !== "0123456789".indexOf(b[0]) ? "\\3" + b[0] + " " + b.substr(1).replace(a.jstree.idregex, "\\$&") : b.replace(a.jstree.idregex, "\\$&")
                        }).join(", #"))), this._data.search.dom.children(".jstree-anchor").addClass("jstree-search"), this._data.search.som && this._data.search.res.length)) {
                            for (d = 0, e = g.length; e > d; d++) h = h.concat(this.get_node(g[d]).parents);
                            h = a.vakata.array_remove_item(a.vakata.array_unique(h), "#"), i = h.length ? a(this.element[0].querySelectorAll("#" + a.map(h, function (b) {
                                return -1 !== "0123456789".indexOf(b[0]) ? "\\3" + b[0] + " " + b.substr(1).replace(a.jstree.idregex, "\\$&") : b.replace(a.jstree.idregex, "\\$&")
                            }).join(", #"))) : a(), this.element.find(".jstree-node").hide().filter(".jstree-last").filter(function () {
                                return this.nextSibling
                            }).removeClass("jstree-last"), i = i.add(this._data.search.dom), i.parentsUntil(".jstree").addBack().show().filter(".jstree-children").each(function () {
                                a(this).children(".jstree-node:visible").eq(-1).addClass("jstree-last")
                            })
                        }
                    }, this)).on("search.jstree", a.proxy(function (b, c) {
                        this._data.search.som && c.nodes.length && (this.element.find(".jstree-node").hide().filter(".jstree-last").filter(function () {
                            return this.nextSibling
                        }).removeClass("jstree-last"), c.nodes.parentsUntil(".jstree").addBack().show().filter(".jstree-children").each(function () {
                            a(this).children(".jstree-node:visible").eq(-1).addClass("jstree-last")
                        }))
                    }, this)).on("clear_search.jstree", a.proxy(function (a, b) {
                        this._data.search.som && b.nodes.length && this.element.find(".jstree-node").css("display", "").filter(".jstree-last").filter(function () {
                            return this.nextSibling
                        }).removeClass("jstree-last")
                    }, this))
                }, this.search = function (c, d, e) {
                    if (c === !1 || "" === a.trim(c.toString())) return this.clear_search();
                    c = c.toString();
                    var f = this.settings.search, g = f.ajax ? f.ajax : !1, h = null, i = [], j = [], k, l;
                    return this._data.search.res.length && this.clear_search(), e === b && (e = f.show_only_matches), d || g === !1 ? (this._data.search.str = c, this._data.search.dom = a(), this._data.search.res = [], this._data.search.opn = [], this._data.search.som = e, h = new a.vakata.search(c, !0, {
                        caseSensitive: f.case_sensitive,
                        fuzzy: f.fuzzy
                    }), a.each(this._model.data, function (a, b) {
                        b.text && (f.search_callback && f.search_callback.call(this, c, b) || !f.search_callback && h.search(b.text).isMatch) && (!f.search_leaves_only || b.state.loaded && 0 === b.children.length) && (i.push(a), j = j.concat(b.parents))
                    }), i.length && (j = a.vakata.array_unique(j), this._search_open(j), this._data.search.dom = a(this.element[0].querySelectorAll("#" + a.map(i, function (b) {
                        return -1 !== "0123456789".indexOf(b[0]) ? "\\3" + b[0] + " " + b.substr(1).replace(a.jstree.idregex, "\\$&") : b.replace(a.jstree.idregex, "\\$&")
                    }).join(", #"))), this._data.search.res = i, this._data.search.dom.children(".jstree-anchor").addClass("jstree-search")), void this.trigger("search", {
                        nodes: this._data.search.dom,
                        str: c,
                        res: this._data.search.res,
                        show_only_matches: e
                    })) : a.isFunction(g) ? g.call(this, c, a.proxy(function (b) {
                        b && b.d && (b = b.d), this._load_nodes(a.isArray(b) ? a.vakata.array_unique(b) : [], function () {
                            this.search(c, !0, e)
                        }, !0)
                    }, this)) : (g = a.extend({}, g), g.data || (g.data = {}), g.data.str = c, a.ajax(g).fail(a.proxy(function () {
                        this._data.core.last_error = {
                            error: "ajax",
                            plugin: "search",
                            id: "search_01",
                            reason: "Could not load search parents",
                            data: JSON.stringify(g)
                        }, this.settings.core.error.call(this, this._data.core.last_error)
                    }, this)).done(a.proxy(function (b) {
                        b && b.d && (b = b.d), this._load_nodes(a.isArray(b) ? a.vakata.array_unique(b) : [], function () {
                            this.search(c, !0, e)
                        }, !0)
                    }, this)))
                }, this.clear_search = function () {
                    this._data.search.dom.children(".jstree-anchor").removeClass("jstree-search"), this.settings.search.close_opened_onclear && this.close_node(this._data.search.opn, 0), this.trigger("clear_search", {
                        nodes: this._data.search.dom,
                        str: this._data.search.str,
                        res: this._data.search.res
                    }), this._data.search.str = "", this._data.search.res = [], this._data.search.opn = [], this._data.search.dom = a()
                }, this._search_open = function (b) {
                    var c = this;
                    a.each(b.concat([]), function (d, e) {
                        if ("#" === e) return !0;
                        try {
                            e = a("#" + e.replace(a.jstree.idregex, "\\$&"), c.element)
                        } catch (f) {
                        }
                        e && e.length && c.is_closed(e) && (c._data.search.opn.push(e[0].id), c.open_node(e, function () {
                            c._search_open(b)
                        }, 0))
                    })
                }
            }, function (a) {
                a.vakata.search = function (a, b, c) {
                    c = c || {}, c.fuzzy !== !1 && (c.fuzzy = !0), a = c.caseSensitive ? a : a.toLowerCase();
                    var d = c.location || 0, e = c.distance || 100, f = c.threshold || .6, g = a.length, h, i, j, k;
                    return g > 32 && (c.fuzzy = !1), c.fuzzy && (h = 1 << g - 1, i = function () {
                        var b = {}, c = 0;
                        for (c = 0; g > c; c++) b[a.charAt(c)] = 0;
                        for (c = 0; g > c; c++) b[a.charAt(c)] |= 1 << g - c - 1;
                        return b
                    }(), j = function (a, b) {
                        var c = a / g, f = Math.abs(d - b);
                        return e ? c + f / e : f ? 1 : c
                    }), k = function (b) {
                        if (b = c.caseSensitive ? b : b.toLowerCase(), a === b || -1 !== b.indexOf(a)) return {
                            isMatch: !0,
                            score: 0
                        };
                        if (!c.fuzzy) return {isMatch: !1, score: 1};
                        var e, k, l = b.length, m = f, n = b.indexOf(a, d), o, p, q = g + l, r, s, t, u, v, w = 1,
                            x = [];
                        for (-1 !== n && (m = Math.min(j(0, n), m), n = b.lastIndexOf(a, d + g), -1 !== n && (m = Math.min(j(0, n), m))), n = -1, e = 0; g > e; e++) {
                            o = 0, p = q;
                            while (p > o) j(e, d + p) <= m ? o = p : q = p, p = Math.floor((q - o) / 2 + o);
                            for (q = p, s = Math.max(1, d - p + 1), t = Math.min(d + p, l) + g, u = new Array(t + 2), u[t + 1] = (1 << e) - 1, k = t; k >= s; k--) if (v = i[b.charAt(k - 1)], u[k] = 0 === e ? (u[k + 1] << 1 | 1) & v : (u[k + 1] << 1 | 1) & v | ((r[k + 1] | r[k]) << 1 | 1) | r[k + 1], u[k] & h && (w = j(e, k - 1), m >= w)) {
                                if (m = w, n = k - 1, x.push(n), !(n > d)) break;
                                s = Math.max(1, 2 * d - n)
                            }
                            if (j(e + 1, d) > m) break;
                            r = u
                        }
                        return {isMatch: n >= 0, score: w}
                    }, b === !0 ? {search: k} : k(b)
                }
            }(a), a.jstree.defaults.sort = function (a, b) {
                return this.get_text(a) > this.get_text(b) ? 1 : -1
            }, a.jstree.plugins.sort = function (b, c) {
                this.bind = function () {
                    c.bind.call(this), this.element.on("model.jstree", a.proxy(function (a, b) {
                        this.sort(b.parent, !0)
                    }, this)).on("rename_node.jstree create_node.jstree", a.proxy(function (a, b) {
                        this.sort(b.parent || b.node.parent, !1), this.redraw_node(b.parent || b.node.parent, !0)
                    }, this)).on("move_node.jstree copy_node.jstree", a.proxy(function (a, b) {
                        this.sort(b.parent, !1), this.redraw_node(b.parent, !0)
                    }, this))
                }, this.sort = function (b, c) {
                    var d, e;
                    if (b = this.get_node(b), b && b.children && b.children.length && (b.children.sort(a.proxy(this.settings.sort, this)), c)) for (d = 0, e = b.children_d.length; e > d; d++) this.sort(b.children_d[d], !1)
                }
            };
            var q = !1;
            a.jstree.defaults.state = {
                key: "jstree",
                events: "changed.jstree open_node.jstree close_node.jstree check_node.jstree uncheck_node.jstree",
                ttl: !1,
                filter: !1
            }, a.jstree.plugins.state = function (b, c) {
                this.bind = function () {
                    c.bind.call(this);
                    var b = a.proxy(function () {
                        this.element.on(this.settings.state.events, a.proxy(function () {
                            q && clearTimeout(q), q = setTimeout(a.proxy(function () {
                                this.save_state()
                            }, this), 100)
                        }, this)), this.trigger("state_ready")
                    }, this);
                    this.element.on("ready.jstree", a.proxy(function (a, c) {
                        this.element.one("restore_state.jstree", b), this.restore_state() || b()
                    }, this))
                }, this.save_state = function () {
                    var b = {state: this.get_state(), ttl: this.settings.state.ttl, sec: +new Date};
                    a.vakata.storage.set(this.settings.state.key, JSON.stringify(b))
                }, this.restore_state = function () {
                    var b = a.vakata.storage.get(this.settings.state.key);
                    if (b) try {
                        b = JSON.parse(b)
                    } catch (c) {
                        return !1
                    }
                    return b && b.ttl && b.sec && +new Date - b.sec > b.ttl ? !1 : (b && b.state && (b = b.state), b && a.isFunction(this.settings.state.filter) && (b = this.settings.state.filter.call(this, b)), b ? (this.element.one("set_state.jstree", function (c, d) {
                        d.instance.trigger("restore_state", {state: a.extend(!0, {}, b)})
                    }), this.set_state(b), !0) : !1)
                }, this.clear_state = function () {
                    return a.vakata.storage.del(this.settings.state.key)
                }
            }, function (a, b) {
                a.vakata.storage = {
                    set: function (a, b) {
                        return window.localStorage.setItem(a, b)
                    }, get: function (a) {
                        return window.localStorage.getItem(a)
                    }, del: function (a) {
                        return window.localStorage.removeItem(a)
                    }
                }
            }(a), a.jstree.defaults.types = {"#": {}, "default": {}}, a.jstree.plugins.types = function (c, d) {
                this.init = function (a, c) {
                    var e, f;
                    if (c && c.types && c.types["default"]) for (e in c.types) if ("default" !== e && "#" !== e && c.types.hasOwnProperty(e)) for (f in c.types["default"]) c.types["default"].hasOwnProperty(f) && c.types[e][f] === b && (c.types[e][f] = c.types["default"][f]);
                    d.init.call(this, a, c), this._model.data["#"].type = "#"
                }, this.refresh = function (a, b) {
                    d.refresh.call(this, a, b), this._model.data["#"].type = "#"
                }, this.bind = function () {
                    this.element.on("model.jstree", a.proxy(function (a, c) {
                        var d = this._model.data, e = c.nodes, f = this.settings.types, g, h, i = "default";
                        for (g = 0, h = e.length; h > g; g++) i = "default", d[e[g]].original && d[e[g]].original.type && f[d[e[g]].original.type] && (i = d[e[g]].original.type), d[e[g]].data && d[e[g]].data.jstree && d[e[g]].data.jstree.type && f[d[e[g]].data.jstree.type] && (i = d[e[g]].data.jstree.type), d[e[g]].type = i, d[e[g]].icon === !0 && f[i].icon !== b && (d[e[g]].icon = f[i].icon);
                        d["#"].type = "#"
                    }, this)), d.bind.call(this)
                }, this.get_json = function (b, c, e) {
                    var f, g, h = this._model.data, i = c ? a.extend(!0, {}, c, {no_id: !1}) : {},
                        j = d.get_json.call(this, b, i, e);
                    if (j === !1) return !1;
                    if (a.isArray(j)) for (f = 0, g = j.length; g > f; f++) j[f].type = j[f].id && h[j[f].id] && h[j[f].id].type ? h[j[f].id].type : "default", c && c.no_id && (delete j[f].id, j[f].li_attr && j[f].li_attr.id && delete j[f].li_attr.id, j[f].a_attr && j[f].a_attr.id && delete j[f].a_attr.id); else j.type = j.id && h[j.id] && h[j.id].type ? h[j.id].type : "default", c && c.no_id && (j = this._delete_ids(j));
                    return j
                }, this._delete_ids = function (b) {
                    if (a.isArray(b)) {
                        for (var c = 0, d = b.length; d > c; c++) b[c] = this._delete_ids(b[c]);
                        return b
                    }
                    return delete b.id, b.li_attr && b.li_attr.id && delete b.li_attr.id, b.a_attr && b.a_attr.id && delete b.a_attr.id, b.children && a.isArray(b.children) && (b.children = this._delete_ids(b.children)), b
                }, this.check = function (c, e, f, g, h) {
                    if (d.check.call(this, c, e, f, g, h) === !1) return !1;
                    e = e && e.id ? e : this.get_node(e), f = f && f.id ? f : this.get_node(f);
                    var i = e && e.id ? a.jstree.reference(e.id) : null, j, k, l, m;
                    switch (i = i && i._model && i._model.data ? i._model.data : null, c) {
                        case"create_node":
                        case"move_node":
                        case"copy_node":
                            if ("move_node" !== c || -1 === a.inArray(e.id, f.children)) {
                                if (j = this.get_rules(f), j.max_children !== b && -1 !== j.max_children && j.max_children === f.children.length) return this._data.core.last_error = {
                                    error: "check",
                                    plugin: "types",
                                    id: "types_01",
                                    reason: "max_children prevents function: " + c,
                                    data: JSON.stringify({
                                        chk: c,
                                        pos: g,
                                        obj: e && e.id ? e.id : !1,
                                        par: f && f.id ? f.id : !1
                                    })
                                }, !1;
                                if (j.valid_children !== b && -1 !== j.valid_children && -1 === a.inArray(e.type || "default", j.valid_children)) return this._data.core.last_error = {
                                    error: "check",
                                    plugin: "types",
                                    id: "types_02",
                                    reason: "valid_children prevents function: " + c,
                                    data: JSON.stringify({
                                        chk: c,
                                        pos: g,
                                        obj: e && e.id ? e.id : !1,
                                        par: f && f.id ? f.id : !1
                                    })
                                }, !1;
                                if (i && e.children_d && e.parents) {
                                    for (k = 0, l = 0, m = e.children_d.length; m > l; l++) k = Math.max(k, i[e.children_d[l]].parents.length);
                                    k = k - e.parents.length + 1
                                }
                                (0 >= k || k === b) && (k = 1);
                                do {
                                    if (j.max_depth !== b && -1 !== j.max_depth && j.max_depth < k) return this._data.core.last_error = {
                                        error: "check",
                                        plugin: "types",
                                        id: "types_03",
                                        reason: "max_depth prevents function: " + c,
                                        data: JSON.stringify({
                                            chk: c,
                                            pos: g,
                                            obj: e && e.id ? e.id : !1,
                                            par: f && f.id ? f.id : !1
                                        })
                                    }, !1;
                                    f = this.get_node(f.parent), j = this.get_rules(f), k++
                                } while (f)
                            }
                    }
                    return !0
                }, this.get_rules = function (a) {
                    if (a = this.get_node(a), !a) return !1;
                    var c = this.get_type(a, !0);
                    return c.max_depth === b && (c.max_depth = -1), c.max_children === b && (c.max_children = -1), c.valid_children === b && (c.valid_children = -1), c
                }, this.get_type = function (b, c) {
                    return b = this.get_node(b), b ? c ? a.extend({type: b.type}, this.settings.types[b.type]) : b.type : !1
                }, this.set_type = function (c, d) {
                    var e, f, g, h, i;
                    if (a.isArray(c)) {
                        for (c = c.slice(), f = 0, g = c.length; g > f; f++) this.set_type(c[f], d);
                        return !0
                    }
                    return e = this.settings.types, c = this.get_node(c), e[d] && c ? (h = c.type, i = this.get_icon(c), c.type = d, (i === !0 || e[h] && e[h].icon !== b && i === e[h].icon) && this.set_icon(c, e[d].icon !== b ? e[d].icon : !0), !0) : !1
                }
            }, a.jstree.defaults.unique = {
                case_sensitive: !1, duplicate: function (a, b) {
                    return a + " (" + b + ")"
                }
            }, a.jstree.plugins.unique = function (c, d) {
                this.check = function (b, c, e, f, g) {
                    if (d.check.call(this, b, c, e, f, g) === !1) return !1;
                    if (c = c && c.id ? c : this.get_node(c), e = e && e.id ? e : this.get_node(e), !e || !e.children) return !0;
                    var h = "rename_node" === b ? f : c.text, i = [], j = this.settings.unique.case_sensitive,
                        k = this._model.data, l, m;
                    for (l = 0, m = e.children.length; m > l; l++) i.push(j ? k[e.children[l]].text : k[e.children[l]].text.toLowerCase());
                    switch (j || (h = h.toLowerCase()), b) {
                        case"delete_node":
                            return !0;
                        case"rename_node":
                            return l = -1 === a.inArray(h, i) || c.text && c.text[j ? "toString" : "toLowerCase"]() === h, l || (this._data.core.last_error = {
                                error: "check",
                                plugin: "unique",
                                id: "unique_01",
                                reason: "Child with name " + h + " already exists. Preventing: " + b,
                                data: JSON.stringify({
                                    chk: b,
                                    pos: f,
                                    obj: c && c.id ? c.id : !1,
                                    par: e && e.id ? e.id : !1
                                })
                            }), l;
                        case"create_node":
                            return l = -1 === a.inArray(h, i), l || (this._data.core.last_error = {
                                error: "check",
                                plugin: "unique",
                                id: "unique_04",
                                reason: "Child with name " + h + " already exists. Preventing: " + b,
                                data: JSON.stringify({
                                    chk: b,
                                    pos: f,
                                    obj: c && c.id ? c.id : !1,
                                    par: e && e.id ? e.id : !1
                                })
                            }), l;
                        case"copy_node":
                            return l = -1 === a.inArray(h, i), l || (this._data.core.last_error = {
                                error: "check",
                                plugin: "unique",
                                id: "unique_02",
                                reason: "Child with name " + h + " already exists. Preventing: " + b,
                                data: JSON.stringify({
                                    chk: b,
                                    pos: f,
                                    obj: c && c.id ? c.id : !1,
                                    par: e && e.id ? e.id : !1
                                })
                            }), l;
                        case"move_node":
                            return l = c.parent === e.id || -1 === a.inArray(h, i), l || (this._data.core.last_error = {
                                error: "check",
                                plugin: "unique",
                                id: "unique_03",
                                reason: "Child with name " + h + " already exists. Preventing: " + b,
                                data: JSON.stringify({
                                    chk: b,
                                    pos: f,
                                    obj: c && c.id ? c.id : !1,
                                    par: e && e.id ? e.id : !1
                                })
                            }), l
                    }
                    return !0
                }, this.create_node = function (c, e, f, g, h) {
                    if (!e || e.text === b) {
                        if (null === c && (c = "#"), c = this.get_node(c), !c) return d.create_node.call(this, c, e, f, g, h);
                        if (f = f === b ? "last" : f, !f.toString().match(/^(before|after)$/) && !h && !this.is_loaded(c)) return d.create_node.call(this, c, e, f, g, h);
                        e || (e = {});
                        var i, j, k, l, m, n = this._model.data, o = this.settings.unique.case_sensitive,
                            p = this.settings.unique.duplicate;
                        for (j = i = this.get_string("New node"), k = [], l = 0, m = c.children.length; m > l; l++) k.push(o ? n[c.children[l]].text : n[c.children[l]].text.toLowerCase());
                        l = 1;
                        while (-1 !== a.inArray(o ? j : j.toLowerCase(), k)) j = p.call(this, i, ++l).toString();
                        e.text = j
                    }
                    return d.create_node.call(this, c, e, f, g, h)
                }
            };
            var r = document.createElement("DIV");
            r.setAttribute("unselectable", "on"), r.setAttribute("role", "presentation"), r.className = "jstree-wholerow", r.innerHTML = "&#160;", a.jstree.plugins.wholerow = function (b, c) {
                this.bind = function () {
                    c.bind.call(this), this.element.on("ready.jstree set_state.jstree", a.proxy(function () {
                        this.hide_dots()
                    }, this)).on("init.jstree loading.jstree ready.jstree", a.proxy(function () {
                        this.get_container_ul().addClass("jstree-wholerow-ul")
                    }, this)).on("deselect_all.jstree", a.proxy(function (a, b) {
                        this.element.find(".jstree-wholerow-clicked").removeClass("jstree-wholerow-clicked")
                    }, this)).on("changed.jstree", a.proxy(function (a, b) {
                        this.element.find(".jstree-wholerow-clicked").removeClass("jstree-wholerow-clicked");
                        var c = !1, d, e;
                        for (d = 0, e = b.selected.length; e > d; d++) c = this.get_node(b.selected[d], !0), c && c.length && c.children(".jstree-wholerow").addClass("jstree-wholerow-clicked")
                    }, this)).on("open_node.jstree", a.proxy(function (a, b) {
                        this.get_node(b.node, !0).find(".jstree-clicked").parent().children(".jstree-wholerow").addClass("jstree-wholerow-clicked")
                    }, this)).on("hover_node.jstree dehover_node.jstree", a.proxy(function (a, b) {
                        "hover_node" === a.type && this.is_disabled(b.node) || this.get_node(b.node, !0).children(".jstree-wholerow")["hover_node" === a.type ? "addClass" : "removeClass"]("jstree-wholerow-hovered")
                    }, this)).on("contextmenu.jstree", ".jstree-wholerow", a.proxy(function (b) {
                        b.preventDefault();
                        var c = a.Event("contextmenu", {
                            metaKey: b.metaKey,
                            ctrlKey: b.ctrlKey,
                            altKey: b.altKey,
                            shiftKey: b.shiftKey,
                            pageX: b.pageX,
                            pageY: b.pageY
                        });
                        a(b.currentTarget).closest(".jstree-node").children(".jstree-anchor").first().trigger(c)
                    }, this)).on("click.jstree", ".jstree-wholerow", function (b) {
                        b.stopImmediatePropagation();
                        var c = a.Event("click", {
                            metaKey: b.metaKey,
                            ctrlKey: b.ctrlKey,
                            altKey: b.altKey,
                            shiftKey: b.shiftKey
                        });
                        a(b.currentTarget).closest(".jstree-node").children(".jstree-anchor").first().trigger(c).focus()
                    }).on("click.jstree", ".jstree-leaf > .jstree-ocl", a.proxy(function (b) {
                        b.stopImmediatePropagation();
                        var c = a.Event("click", {
                            metaKey: b.metaKey,
                            ctrlKey: b.ctrlKey,
                            altKey: b.altKey,
                            shiftKey: b.shiftKey
                        });
                        a(b.currentTarget).closest(".jstree-node").children(".jstree-anchor").first().trigger(c).focus()
                    }, this)).on("mouseover.jstree", ".jstree-wholerow, .jstree-icon", a.proxy(function (a) {
                        return a.stopImmediatePropagation(), this.is_disabled(a.currentTarget) || this.hover_node(a.currentTarget), !1
                    }, this)).on("mouseleave.jstree", ".jstree-node", a.proxy(function (a) {
                        this.dehover_node(a.currentTarget)
                    }, this))
                }, this.teardown = function () {
                    this.settings.wholerow && this.element.find(".jstree-wholerow").remove(), c.teardown.call(this)
                }, this.redraw_node = function (b, d, e, f) {
                    if (b = c.redraw_node.apply(this, arguments)) {
                        var g = r.cloneNode(!0);
                        -1 !== a.inArray(b.id, this._data.core.selected) && (g.className += " jstree-wholerow-clicked"), this._data.core.focused && this._data.core.focused === b.id && (g.className += " jstree-wholerow-hovered"), b.insertBefore(g, b.childNodes[0])
                    }
                    return b
                }
            }, function (a) {
                if (document.registerElement && Object && Object.create) {
                    var b = Object.create(HTMLElement.prototype);
                    b.createdCallback = function () {
                        var b = {core: {}, plugins: []}, c;
                        for (c in a.jstree.plugins) a.jstree.plugins.hasOwnProperty(c) && this.attributes[c] && (b.plugins.push(c), this.getAttribute(c) && JSON.parse(this.getAttribute(c)) && (b[c] = JSON.parse(this.getAttribute(c))));
                        for (c in a.jstree.defaults.core) a.jstree.defaults.core.hasOwnProperty(c) && this.attributes[c] && (b.core[c] = JSON.parse(this.getAttribute(c)) || this.getAttribute(c));
                        jQuery(this).jstree(b)
                    };
                    try {
                        document.registerElement("vakata-jstree", {prototype: b})
                    } catch (c) {
                    }
                }
            }(jQuery)
        }
    });
}