
(function() {
  var fn = function() {
    Bokeh.safely(function() {
    var docs_json = {"b0aa03bf-752d-4a99-8e49-04df9fb21528":{"roots":{"references":[{"attributes":{"plot":{"id":"77acadae-3dec-4807-aff9-8c57b26d3d05","subtype":"Figure","type":"Plot"}},"id":"04e494c2-53a8-4e05-a36c-2bbe27281d56","type":"ResetTool"},{"attributes":{"callback":null},"id":"5fb3adef-cd46-43be-b0dc-23a595792e4f","type":"DataRange1d"},{"attributes":{"line_alpha":{"value":0.1},"line_color":{"value":"#1f77b4"},"line_width":{"value":2},"x":{"field":"x"},"y":{"field":"y"}},"id":"517468a3-2564-4fc0-894e-e40c5168898c","type":"Line"},{"attributes":{"formatter":{"id":"baef4f1e-e1bb-4fa8-8347-3806fb0b0eac","type":"BasicTickFormatter"},"plot":{"id":"77acadae-3dec-4807-aff9-8c57b26d3d05","subtype":"Figure","type":"Plot"},"ticker":{"id":"e2bcc50a-3d2a-4038-946f-8d622c0820e2","type":"BasicTicker"}},"id":"3cca8e77-b1c5-48d5-899b-0dacaeabad5e","type":"LinearAxis"},{"attributes":{"plot":{"id":"77acadae-3dec-4807-aff9-8c57b26d3d05","subtype":"Figure","type":"Plot"}},"id":"43849486-f7fb-49cc-adfa-794ecf4d1038","type":"SaveTool"},{"attributes":{"active_drag":"auto","active_inspect":"auto","active_scroll":"auto","active_tap":"auto","tools":[{"id":"ab9a0a35-1002-4070-9663-bc537c5c8ffb","type":"PanTool"},{"id":"24657c3f-3f60-4499-98d0-74ecba37e00c","type":"WheelZoomTool"},{"id":"519de9e0-7b5a-4697-a5e6-30d0673231a5","type":"BoxZoomTool"},{"id":"43849486-f7fb-49cc-adfa-794ecf4d1038","type":"SaveTool"},{"id":"04e494c2-53a8-4e05-a36c-2bbe27281d56","type":"ResetTool"},{"id":"11a29b50-0ce0-4b6f-90cc-73fdb6b31142","type":"HelpTool"}]},"id":"bd2cd9fb-cb02-4245-a563-0b97b9d94747","type":"Toolbar"},{"attributes":{},"id":"802528d4-a2bd-48d5-b28f-f26924c564d1","type":"ToolEvents"},{"attributes":{"plot":null,"text":""},"id":"b4e3109d-ef9b-4a41-8b57-f7824d4a9a16","type":"Title"},{"attributes":{"callback":null,"column_names":["x","y"],"data":{"x":[2012,2013,2014],"y":[33563,33636,33599]}},"id":"044c356f-daee-40bb-8bca-86febe040222","type":"ColumnDataSource"},{"attributes":{},"id":"7ba01edc-ca42-4348-b53d-3d3edcc98310","type":"LinearScale"},{"attributes":{"callback":null},"id":"ca4cf19a-3787-45d2-bc39-204985e368ed","type":"DataRange1d"},{"attributes":{"bottom_units":"screen","fill_alpha":{"value":0.5},"fill_color":{"value":"lightgrey"},"left_units":"screen","level":"overlay","line_alpha":{"value":1.0},"line_color":{"value":"black"},"line_dash":[4,4],"line_width":{"value":2},"plot":null,"render_mode":"css","right_units":"screen","top_units":"screen"},"id":"6ee720d1-d93b-426f-8aae-1a6ed117179d","type":"BoxAnnotation"},{"attributes":{},"id":"e2bcc50a-3d2a-4038-946f-8d622c0820e2","type":"BasicTicker"},{"attributes":{},"id":"8edb0218-bcbc-41d6-a0fb-ec8518e5299e","type":"BasicTicker"},{"attributes":{"plot":{"id":"77acadae-3dec-4807-aff9-8c57b26d3d05","subtype":"Figure","type":"Plot"}},"id":"11a29b50-0ce0-4b6f-90cc-73fdb6b31142","type":"HelpTool"},{"attributes":{"line_color":{"value":"#1f77b4"},"line_width":{"value":2},"x":{"field":"x"},"y":{"field":"y"}},"id":"c21807f6-e480-40b2-a17f-7e09a7c246d3","type":"Line"},{"attributes":{"plot":{"id":"77acadae-3dec-4807-aff9-8c57b26d3d05","subtype":"Figure","type":"Plot"}},"id":"ab9a0a35-1002-4070-9663-bc537c5c8ffb","type":"PanTool"},{"attributes":{"plot":{"id":"77acadae-3dec-4807-aff9-8c57b26d3d05","subtype":"Figure","type":"Plot"}},"id":"24657c3f-3f60-4499-98d0-74ecba37e00c","type":"WheelZoomTool"},{"attributes":{"dimension":1,"plot":{"id":"77acadae-3dec-4807-aff9-8c57b26d3d05","subtype":"Figure","type":"Plot"},"ticker":{"id":"e2bcc50a-3d2a-4038-946f-8d622c0820e2","type":"BasicTicker"}},"id":"059c4d66-98fe-42b8-9624-0acb9d515fde","type":"Grid"},{"attributes":{},"id":"baef4f1e-e1bb-4fa8-8347-3806fb0b0eac","type":"BasicTickFormatter"},{"attributes":{"plot":{"id":"77acadae-3dec-4807-aff9-8c57b26d3d05","subtype":"Figure","type":"Plot"},"ticker":{"id":"8edb0218-bcbc-41d6-a0fb-ec8518e5299e","type":"BasicTicker"}},"id":"408cd565-98c9-41ea-b63a-163a60dcc624","type":"Grid"},{"attributes":{},"id":"5b23c291-623e-4c54-a8d7-c44b4b38e5a0","type":"LinearScale"},{"attributes":{"data_source":{"id":"044c356f-daee-40bb-8bca-86febe040222","type":"ColumnDataSource"},"glyph":{"id":"c21807f6-e480-40b2-a17f-7e09a7c246d3","type":"Line"},"hover_glyph":null,"muted_glyph":null,"nonselection_glyph":{"id":"517468a3-2564-4fc0-894e-e40c5168898c","type":"Line"},"selection_glyph":null},"id":"29494fa0-75cb-48f9-a010-b108e614f44f","type":"GlyphRenderer"},{"attributes":{"formatter":{"id":"cb9f80d2-d1d2-4e55-8cb6-33867bc09db9","type":"BasicTickFormatter"},"plot":{"id":"77acadae-3dec-4807-aff9-8c57b26d3d05","subtype":"Figure","type":"Plot"},"ticker":{"id":"8edb0218-bcbc-41d6-a0fb-ec8518e5299e","type":"BasicTicker"}},"id":"bdb6da61-94d4-4c0c-8bf3-187565a6819c","type":"LinearAxis"},{"attributes":{"overlay":{"id":"6ee720d1-d93b-426f-8aae-1a6ed117179d","type":"BoxAnnotation"},"plot":{"id":"77acadae-3dec-4807-aff9-8c57b26d3d05","subtype":"Figure","type":"Plot"}},"id":"519de9e0-7b5a-4697-a5e6-30d0673231a5","type":"BoxZoomTool"},{"attributes":{},"id":"cb9f80d2-d1d2-4e55-8cb6-33867bc09db9","type":"BasicTickFormatter"},{"attributes":{"below":[{"id":"bdb6da61-94d4-4c0c-8bf3-187565a6819c","type":"LinearAxis"}],"left":[{"id":"3cca8e77-b1c5-48d5-899b-0dacaeabad5e","type":"LinearAxis"}],"plot_height":400,"plot_width":400,"renderers":[{"id":"bdb6da61-94d4-4c0c-8bf3-187565a6819c","type":"LinearAxis"},{"id":"408cd565-98c9-41ea-b63a-163a60dcc624","type":"Grid"},{"id":"3cca8e77-b1c5-48d5-899b-0dacaeabad5e","type":"LinearAxis"},{"id":"059c4d66-98fe-42b8-9624-0acb9d515fde","type":"Grid"},{"id":"6ee720d1-d93b-426f-8aae-1a6ed117179d","type":"BoxAnnotation"},{"id":"29494fa0-75cb-48f9-a010-b108e614f44f","type":"GlyphRenderer"}],"title":{"id":"b4e3109d-ef9b-4a41-8b57-f7824d4a9a16","type":"Title"},"tool_events":{"id":"802528d4-a2bd-48d5-b28f-f26924c564d1","type":"ToolEvents"},"toolbar":{"id":"bd2cd9fb-cb02-4245-a563-0b97b9d94747","type":"Toolbar"},"x_range":{"id":"5fb3adef-cd46-43be-b0dc-23a595792e4f","type":"DataRange1d"},"x_scale":{"id":"5b23c291-623e-4c54-a8d7-c44b4b38e5a0","type":"LinearScale"},"y_range":{"id":"ca4cf19a-3787-45d2-bc39-204985e368ed","type":"DataRange1d"},"y_scale":{"id":"7ba01edc-ca42-4348-b53d-3d3edcc98310","type":"LinearScale"}},"id":"77acadae-3dec-4807-aff9-8c57b26d3d05","subtype":"Figure","type":"Plot"}],"root_ids":["77acadae-3dec-4807-aff9-8c57b26d3d05"]},"title":"Bokeh Application","version":"0.12.6"}};
    var render_items = [{"docid":"b0aa03bf-752d-4a99-8e49-04df9fb21528","elementid":"1154c37f-4f4c-4bcc-ace0-d1a24e5c18ab","modelid":"77acadae-3dec-4807-aff9-8c57b26d3d05"}];
  
    Bokeh.embed.embed_items(docs_json, render_items);
  });
};
if (document.readyState != "loading") fn();
else document.addEventListener("DOMContentLoaded", fn);
})();
        