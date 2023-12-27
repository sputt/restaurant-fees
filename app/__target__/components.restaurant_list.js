// Transcrypt'ed from Python, 2023-12-27 16:24:52
var logging = {};
import {AssertionError, AttributeError, BaseException, DeprecationWarning, Exception, IndexError, IterableError, KeyError, NotImplementedError, RuntimeWarning, StopIteration, UserWarning, ValueError, Warning, __JsIterator__, __PyIterator__, __Terminal__, __add__, __and__, __call__, __class__, __envir__, __eq__, __floordiv__, __ge__, __get__, __getcm__, __getitem__, __getslice__, __getsm__, __gt__, __i__, __iadd__, __iand__, __idiv__, __ijsmod__, __ilshift__, __imatmul__, __imod__, __imul__, __in__, __init__, __ior__, __ipow__, __irshift__, __isub__, __ixor__, __jsUsePyNext__, __jsmod__, __k__, __kwargtrans__, __le__, __lshift__, __lt__, __matmul__, __mergefields__, __mergekwargtrans__, __mod__, __mul__, __ne__, __neg__, __nest__, __or__, __pow__, __pragma__, __proxy__, __pyUseJsNext__, __rshift__, __setitem__, __setproperty__, __setslice__, __sort__, __specialattrib__, __sub__, __super__, __t__, __terminal__, __truediv__, __withblock__, __xor__, abs, all, any, assert, bool, bytearray, bytes, callable, chr, copy, deepcopy, delattr, dict, dir, divmod, enumerate, filter, float, format, getattr, hasattr, input, int, isinstance, issubclass, len, list, map, max, min, object, ord, pow, print, property, py_TypeError, py_iter, py_metatype, py_next, py_reversed, py_typeof, range, repr, round, set, setattr, sorted, str, sum, tuple, zip} from './org.transcrypt.__runtime__.js';
import {fetch_template} from './stubs.js';
import {BaseComponent} from './component.js';
import * as __module_logging__ from './logging.js';
__nest__ (logging, '', __module_logging__);
var __name__ = 'components.restaurant_list';
export var RestaurantList =  __class__ ('RestaurantList', [BaseComponent], {
	__module__: __name__,
	props: ['restaurants', 'filter'],
	get __init__ () {return __get__ (this, function (self, restaurants, filter) {
		if (typeof restaurants == 'undefined' || (restaurants != null && restaurants.hasOwnProperty ("__kwargtrans__"))) {;
			var restaurants = null;
		};
		if (typeof filter == 'undefined' || (filter != null && filter.hasOwnProperty ("__kwargtrans__"))) {;
			var filter = null;
		};
		__super__ (RestaurantList, '__init__') (self);
		self.restaurants = restaurants;
		self.filter = filter;
		self.logger = logging.getLogger ('component.restaurant_list');
	}, '__init__');},
	get _get_filtered_restaurants () {return __get__ (this, function (self) {
		return self.restaurants;
	}, '_get_filtered_restaurants');},
	get template () {return async function () {
		return await fetch_template ('templates/restaurant-list.html');
	};}
});
Object.defineProperty (RestaurantList, 'filtered_restaurants', property.call (RestaurantList, RestaurantList._get_filtered_restaurants));;

//# sourceMappingURL=components.restaurant_list.map