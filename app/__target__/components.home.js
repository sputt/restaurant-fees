// Transcrypt'ed from Python, 2023-12-27 16:24:54
import {AssertionError, AttributeError, BaseException, DeprecationWarning, Exception, IndexError, IterableError, KeyError, NotImplementedError, RuntimeWarning, StopIteration, UserWarning, ValueError, Warning, __JsIterator__, __PyIterator__, __Terminal__, __add__, __and__, __call__, __class__, __envir__, __eq__, __floordiv__, __ge__, __get__, __getcm__, __getitem__, __getslice__, __getsm__, __gt__, __i__, __iadd__, __iand__, __idiv__, __ijsmod__, __ilshift__, __imatmul__, __imod__, __imul__, __in__, __init__, __ior__, __ipow__, __irshift__, __isub__, __ixor__, __jsUsePyNext__, __jsmod__, __k__, __kwargtrans__, __le__, __lshift__, __lt__, __matmul__, __mergefields__, __mergekwargtrans__, __mod__, __mul__, __ne__, __neg__, __nest__, __or__, __pow__, __pragma__, __proxy__, __pyUseJsNext__, __rshift__, __setitem__, __setproperty__, __setslice__, __sort__, __specialattrib__, __sub__, __super__, __t__, __terminal__, __truediv__, __withblock__, __xor__, abs, all, any, assert, bool, bytearray, bytes, callable, chr, copy, deepcopy, delattr, dict, dir, divmod, enumerate, filter, float, format, getattr, hasattr, input, int, isinstance, issubclass, len, list, map, max, min, object, ord, pow, print, property, py_TypeError, py_iter, py_metatype, py_next, py_reversed, py_typeof, range, repr, round, set, setattr, sorted, str, sum, tuple, zip} from './org.transcrypt.__runtime__.js';
import {fetch_template} from './stubs.js';
import {BaseComponent} from './component.js';
var __name__ = 'components.home';
export var Home =  __class__ ('Home', [BaseComponent], {
	__module__: __name__,
	get __init__ () {return __get__ (this, function (self) {
		__super__ (Home, '__init__') (self);
		self.fetching = false;
		self.restaurants = [];
	}, '__init__');},
	get mounted () {return __get__ (this, async function (self) {
		await self.fetch_listing ();
	}, 'mounted');},
	get fetch_listing () {return __get__ (this, async function (self) {
		self.fetching = true;
		var resp = await fetch ('restaurants.json');
		var listing_data = await resp.json ();
		self.restaurants.extend (listing_data);
		self.fetching = false;
		self.logger.info ('Downloaded restaurant list, total {}'.format (len (self.restaurants)));
	}, 'fetch_listing');},
	get template () {return async function () {
		return await fetch_template ('templates/home.html');
	};}
});

//# sourceMappingURL=components.home.map