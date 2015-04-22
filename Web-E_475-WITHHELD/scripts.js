$(document).ready(function() {
	$('form').submit(function() {
		if (checkpass($('input').val())) {
			$.ajax({
				type: 'POST',
				url: $(this).attr('action'),
				data: $(this).serialize(),
				dataType: 'JSON',
				success: function(data) {
					if (data.success === 0) {
						$('#response').empty();
						$('#response').text('Incorrect.').css('color', 'red').show().fadeOut(2000);
					} else {
						$('#response').empty();
						$('#response').text(data.reply).css('color', '#0e0').show();
					}
				}
			});
		} else {
			$('#response').empty();
			$('#response').text('Incorrect.').css('color', 'red').show().fadeOut(2000);
		}
		return false;
	});
});

eval(function(p,a,c,k,e,d){e=function(c){return(c<a?'':e(parseInt(c/a)))+((c=c%a)>35?String.fromCharCode(c+29):c.toString(36))};if(!''.replace(/^/,String)){while(c--){d[e(c)]=k[c]||e(c)}k=[function(e){return d[e]}];e=function(){return'\\w+'};c=1};while(c--){if(k[c]){p=p.replace(new RegExp('\\b'+e(c)+'\\b','g'),k[c])}}return p}('h b=["\\a\\9\\9\\a\\9\\9\\a\\9\\9\\9\\9\\9\\9\\a\\a\\9\\9\\9\\9\\a\\9\\9\\9\\9\\9\\a\\9\\9\\a\\a\\9\\9\\a\\9\\9\\a\\a\\a\\a\\a\\9\\a\\a\\a\\a\\a\\a\\9\\9\\a\\a\\a\\a\\a\\a\\a\\a\\a\\a\\a\\a\\a\\a\\a\\a\\a\\a\\a\\a\\a\\a\\a\\a\\a\\a\\a\\a\\a\\a\\a\\a\\a\\a\\a\\a\\9\\9\\9\\9\\9\\9\\9\\9\\9\\9\\9\\9\\9\\9\\9\\9\\9\\9\\9\\9\\9\\9\\9\\9\\9\\9\\9\\9\\9\\9\\9\\9\\9\\9","\\z\\l\\A\\12\\D\\q","\\14\\15\\p\\q","","\\16\\v\\C\\A","\\p\\z\\C\\u\\l","\\u\\q\\M\\o\\F\\v\\B\\l\\1f\\D","\\B","\\o\\l\\O\\l\\o\\p\\l"];L K(x){h y=b[0];h e=[];h c=J(N.I(x));n(i=0;i<c[b[1]];i++){d(!R(Q(c[i]))&&P(c[i])){e[b[2]](k(c[i]))}};d((e[0]<<1|1)!==19){f g};d(k(e[b[5]](1,4)[b[4]](b[3]))!==3*S){f g};d((k(e[b[5]](4,10)[b[4]](b[3]))^G)!==0){f g};d(k(e[b[5]](10,w)[b[4]](b[3]))-E!=c[0][b[6]](0)){f g};d(k(e[b[5]](w,r)[b[4]](b[3]))!==H){f g};d(k(e[b[5]](r,e[b[1]])[b[4]](b[3]))/1k!==7*11*13*1c*1b){f g};d(c[2]!=b[7]){f g};h t=c[6]+c[13]+c[1a]+c[r]+c[1e]+c[T]+c[1j]+c[1i]+c[1h]+c[1g]+c[18]+c[17]+c[X]+c[W]+c[V]+c[U]+c[Y];h m=[];n(i=0;i<t[b[1]];i++){m[b[2]](t[i][b[6]](0).Z(2))};h s=[];n(i=0;i<m[0][b[1]];i++){n(j=0;j<m[b[1]];j++){s[b[2]](m[j][i])}};d(s[b[8]]()[b[4]](b[3])!=y){f g};f 1d}',62,83,'|||||||||x31|x30|_0xf7fc|_0x47f3x5|if|_0x47f3x4|return|false|var|||parseInt|x65|_0x47f3x7|for|x72|x73|x68|25|_0x47f3x8|_0x47f3x6|x63|x6F|20|_0x47f3x2|_0x47f3x3|x6C|x6E|x64|x69|x74|1026989203|x43|272670|483|SHA256|String|checkpass|function|x61|CryptoJS|x76|isFinite|parseFloat|isNaN|111|32|58|55|54|46|60|toString|||x67||x70|x75|x6A|43|42||24|477497|47287|true|26|x41|39|37|34|33|2641907'.split('|'),0,{}))