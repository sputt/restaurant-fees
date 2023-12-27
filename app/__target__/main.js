// Transcrypt'ed from Python, 2023-12-27 16:24:52
var logging = {};
import {AssertionError, AttributeError, BaseException, DeprecationWarning, Exception, IndexError, IterableError, KeyError, NotImplementedError, RuntimeWarning, StopIteration, UserWarning, ValueError, Warning, __JsIterator__, __PyIterator__, __Terminal__, __add__, __and__, __call__, __class__, __envir__, __eq__, __floordiv__, __ge__, __get__, __getcm__, __getitem__, __getslice__, __getsm__, __gt__, __i__, __iadd__, __iand__, __idiv__, __ijsmod__, __ilshift__, __imatmul__, __imod__, __imul__, __in__, __init__, __ior__, __ipow__, __irshift__, __isub__, __ixor__, __jsUsePyNext__, __jsmod__, __k__, __kwargtrans__, __le__, __lshift__, __lt__, __matmul__, __mergefields__, __mergekwargtrans__, __mod__, __mul__, __ne__, __neg__, __nest__, __or__, __pow__, __pragma__, __proxy__, __pyUseJsNext__, __rshift__, __setitem__, __setproperty__, __setslice__, __sort__, __specialattrib__, __sub__, __super__, __t__, __terminal__, __truediv__, __withblock__, __xor__, abs, all, any, assert, bool, bytearray, bytes, callable, chr, copy, deepcopy, delattr, dict, dir, divmod, enumerate, filter, float, format, getattr, hasattr, input, int, isinstance, issubclass, len, list, map, max, min, object, ord, pow, print, property, py_TypeError, py_iter, py_metatype, py_next, py_reversed, py_typeof, range, repr, round, set, setattr, sorted, str, sum, tuple, zip} from './org.transcrypt.__runtime__.js';
import {router} from './routes.js';
import {RestaurantList} from './components.restaurant_list.js';
import {Home} from './components.home.js';
import {Restaurant} from './components.restaurant.js';
import {BaseComponent} from './component.js';
import {Vue, VueRouter} from './third_party.js';
import * as __module_logging__ from './logging.js';
__nest__ (logging, '', __module_logging__);
import {groupby} from './itertools.js';
import {datetime} from './datetime.js';
var __name__ = '__main__';
logging.basicConfig ();
logging.getLogger ().setLevel (logging.DEBUG);
export var TIMEZONE = 'UTC';
export var Version =  __class__ ('Version', [BaseComponent], {
	__module__: __name__,
	props: ['session'],
	get template () {return async function () {
		return '\n            <span>\n                1.0\n            </span>\n            ';
	};}
});
export var RootObject =  __class__ ('RootObject', [object], {
	__module__: __name__,
});
export var _filter_datetime = function (value) {
	var time_obj = datetime.strptime (value, '%Y-%m-%dT%H:%M:%S.%f');
	return (time_obj.strftime ('%Y-%m-%d %H:%M:%S') + ' ') + str (TIMEZONE);
};
export var _filter_json = function (value) {
	var result = null;
	result = JSON.stringify(value, null, 2)
	return result;
};
export var main = function () {
	var root = RootObject ();
	router.afterEach (root.on_route_change);
	Vue.filter ('datetime', _filter_datetime);
	Vue.filter ('pretty', _filter_json);
	var app = new Vue (dict ({'el': '#app', 'data': root, 'methods': dict ({'toggle_menu': (function __lambda__ () {
		return root.toggle_menu ();
	})}), 'router': router}));
};

//# sourceMappingURL=main.map