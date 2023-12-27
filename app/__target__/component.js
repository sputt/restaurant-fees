// Transcrypt'ed from Python, 2023-12-27 16:24:52
var logging = {};
import {AssertionError, AttributeError, BaseException, DeprecationWarning, Exception, IndexError, IterableError, KeyError, NotImplementedError, RuntimeWarning, StopIteration, UserWarning, ValueError, Warning, __JsIterator__, __PyIterator__, __Terminal__, __add__, __and__, __call__, __class__, __envir__, __eq__, __floordiv__, __ge__, __get__, __getcm__, __getitem__, __getslice__, __getsm__, __gt__, __i__, __iadd__, __iand__, __idiv__, __ijsmod__, __ilshift__, __imatmul__, __imod__, __imul__, __in__, __init__, __ior__, __ipow__, __irshift__, __isub__, __ixor__, __jsUsePyNext__, __jsmod__, __k__, __kwargtrans__, __le__, __lshift__, __lt__, __matmul__, __mergefields__, __mergekwargtrans__, __mod__, __mul__, __ne__, __neg__, __nest__, __or__, __pow__, __pragma__, __proxy__, __pyUseJsNext__, __rshift__, __setitem__, __setproperty__, __setslice__, __sort__, __specialattrib__, __sub__, __super__, __t__, __terminal__, __truediv__, __withblock__, __xor__, abs, all, any, assert, bool, bytearray, bytes, callable, chr, copy, deepcopy, delattr, dict, dir, divmod, enumerate, filter, float, format, getattr, hasattr, input, int, isinstance, issubclass, len, list, map, max, min, object, ord, pow, print, property, py_TypeError, py_iter, py_metatype, py_next, py_reversed, py_typeof, range, repr, round, set, setattr, sorted, str, sum, tuple, zip} from './org.transcrypt.__runtime__.js';
import {Vue} from './third_party.js';
import * as __module_logging__ from './logging.js';
__nest__ (logging, '', __module_logging__);
var __name__ = 'component';
export var ALL_CLASSES = [];
export var instance_wrapper = function (func) {
	if (__t__ (__envir__.executor_name == 'transcrypt')) {
		var wrapper = function (arg1, arg2, arg3, arg4) {
			var wrapped_args = [];
			if (__t__ (arg1 != undefined
			)) {
				wrapped_args.append (arg1);
			}
			if (__t__ (arg2 != undefined
			)) {
				wrapped_args.append (arg2);
			}
			if (__t__ (arg3 != undefined
			)) {
				wrapped_args.append (arg3);
			}
			if (__t__ (arg4 != undefined
			)) {
				wrapped_args.append (arg4);
			}
			return func (this, ...wrapped_args);
		};
		return wrapper;
	}
	else {
		return func;
	}
};
export var DataSubscriptions =  __class__ ('DataSubscriptions', [object], {
	__module__: __name__,
});
export var ComponentMeta =  __class__ ('ComponentMeta', [py_metatype], {
	__module__: __name__,
	get __new__ () {return __get__ (this, function (meta, py_name, bases, attribs) {
		var result = py_metatype.__new__ (meta, py_name, bases, attribs);
		if (__t__ (!__in__ (py_name, tuple (['BaseComponent', 'HydraComponent', 'HydraDuplexComponent'])))) {
			result.register ();
			ALL_CLASSES.append (result);
		}
		return result;
	}, '__new__');}
});
export var BaseComponent =  __class__ ('BaseComponent', [object], {
	__module__: __name__,
	props: [],
	subscriptions: dict ({}),
	get __init__ () {return __get__ (this, function (self) {
		self._watches = dict ({});
		self.logger = logging.getLogger ('component').getChild (self.__class__.__name__.lower ());
	}, '__init__');},
	get _create_state () {return __get__ (this, function (self, component, methods, computed) {
		if (__t__ (__envir__.executor_name == 'transcrypt')) {
			var data_subscriptions = new Object ();
		}
		else {
			var data_subscriptions = DataSubscriptions ();
			data_subscriptions.__class__ = self.__class__;
		}
		for (var data of __i__ (dir (self))) {
			if (__t__ (__in__ (data, tuple (['props'])))) {
				continue;
			}
			if (__t__ (__t__ (data.startswith ('__')) || data.startswith ('_get_'))) {
				continue;
			}
			if (__t__ (__t__ (__in__ (data, methods)) || __t__ (__in__ (data, computed)) || __in__ (data, self.__class__.props))) {
				continue;
			}
			setattr (data_subscriptions, data, getattr (self, data));
		}
		return data_subscriptions;
	}, '_create_state');},
	get watch () {return __get__ (this, function (self, prop_or_data, meth, deep) {
		if (typeof deep == 'undefined' || (deep != null && deep.hasOwnProperty ("__kwargtrans__"))) {;
			var deep = false;
		};
		var options = dict ({'deep': deep});
		self.$watch (prop_or_data, instance_wrapper (meth), options);
	}, 'watch');},
	get emit () {return __get__ (this, function (self, event_name, value) {
		self.$emit (event_name, value);
	}, 'emit');},
	get force_update () {return __get__ (this, function (self) {
		self.$forceUpdate ();
	}, 'force_update');},
	get register () {return __getcm__ (this, function (cls) {
		var all_methods = dict ({});
		var all_computed = dict ({});
		var _create_state = function (component) {
			if (typeof component == 'undefined' || (component != null && component.hasOwnProperty ("__kwargtrans__"))) {;
				var component = null;
			};
			if (__t__ (!__t__ ((component)))) {
				var component = this;
			}
			var kwargs = dict ({});
			for (var prop of __i__ (cls.props)) {
				kwargs [prop] = getattr (component, prop);
			}
			var self = cls (__kwargtrans__ (kwargs));
			self.logger.info ('Calling create state');
			var result = self._create_state (component, all_methods, all_computed);
			if (__t__ (__envir__.executor_name != 'transcrypt')) {
				for (var prop of __i__ (cls.props)) {
					setattr (result, prop, getattr (component, prop, null));
				}
			}
			return result;
		};
		var _creator = async function (resolve, reject) {
			try {
				for (var attr of __i__ (dir (cls))) {
					if (__t__ (attr.startswith ('__'))) {
						continue;
					}
					if (__t__ (hasattr (cls, '_get_' + attr))) {
						continue;
					}
					if (__t__ (callable (getattr (cls, attr)))) {
						var meth = getattr (cls, attr);
						if (__t__ (attr.startswith ('_get_'))) {
							var prop_name = attr.py_replace ('_get_', '');
							all_computed [prop_name] = meth;
						}
						else {
							all_methods [attr] = instance_wrapper (meth);
						}
					}
					if (__t__ (__envir__.executor_name != 'transcrypt')) {
						if (__t__ (isinstance (getattr (cls, attr), property))) {
							all_computed [attr] = getattr (cls, attr).fget;
						}
					}
				}
				print ('Resolving creator: {}'.format (cls.__name__));
				var resolved_template = await cls.template ();
				if (__t__ (!__t__ ((resolved_template)))) {
					reject (ValueError ('Must provide a template'));
					return ;
				}
				resolve (dict ({'props': cls.props, 'mounted': all_methods.py_get ('mounted', (function __lambda__ () {
					return null;
				})), 'destroyed': all_methods.py_get ('destroyed', (function __lambda__ () {
					return null;
				})), 'methods': all_methods, 'computed': all_computed, 'data': _create_state, 'watch': dict ({'$route': all_methods.py_get ('route_changed', (function __lambda__ () {
					var args = tuple ([].slice.apply (arguments).slice (0));
					return null;
				}))}), 'template': resolved_template}));
			}
			catch (__except0__) {
				reject ('FAILURE');
			}
		};
		Vue.component (cls.__name__, _creator);
	}, 'register');},
	get template () {return async function () {
		var __except0__ = NotImplementedError;
		__except0__.__cause__ = null;
		throw __except0__;
	};}
}, ComponentMeta);

//# sourceMappingURL=component.map