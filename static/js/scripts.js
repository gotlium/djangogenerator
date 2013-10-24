/**
 * Created by gotlium on 24.10.13.
 */

(function ($) {
    showHideAdminOptions = function () {
        var showHideFields = function (form, status) {
            form.find('label').each(function () {
                var element = $(this).parent();
                var selectLen = element.find('select').length;
                var indexOfAdmin = $(this).text().indexOf('Admin');
                if (indexOfAdmin > -1 || selectLen) {
                    if (status) {
                        element.show();
                    } else {
                        element.hide();
                    }
                    ;
                }
                ;
            });
        };

        $('form').each(function () {
            var form = $(this);
            form.find('select').each(function () {
                if ($(this).attr('id').indexOf('index_together') != -1) {
                    if ($(this).find('option').length > 0) {
                        showHideFields(form, true);
                    } else {
                        showHideFields(form, false);
                    }
                    ;
                    return 0;
                }
                ;
            });
        });
    };


    var modifiedUnlock = function () {
        setTimeout(function () {
            modifiedLock = false;
        }, 1000);
    };

    reloadSelectValues = function () {
        var models = [];

        $('form').each(function () {
            if ($(this).attr('id').indexOf('model_') == 0) {
                models.push($(this).attr('id').split('_')[1]);
            }
            ;
        });

        $.each(models, function (index, modelId) {
            $.ajax({
                url: '/model/get/' + modelId + '/',
                dataType: "json",
                success: function (data) {
                    if (data && data.length) {
                        var form_sel = '#model_' + modelId + '_form select';
                        $(form_sel).each(function () {
                            var select = $(this);
                            if (select.attr('id').indexOf('model') != -1) {
                                $.each(data, function (i, row) {
                                    if (select.find("option[value='" + row[0] + "']").length == 0) {
                                        select.append(
                                            '<option value="' + row[0] + '">' + row[1] + '</option>'
                                        );
                                    }
                                    ;
                                });
                            }
                            ;
                        });
                    }
                    ;
                }
            });
        });

        modifiedUnlock();
        showHideAdminOptions();
    };


    modifiedLock = false;
    $(document).bind('DOMSubtreeModified', function () {
        if (!modifiedLock) {
            modifiedLock = true;
            reloadSelectValues();
        }
    });

    $(document).ajaxComplete(function () {
        showHideAdminOptions();
    });

    $(document).ready(function () {
        showHideAdminOptions();
    });


})(jQuery);


window.onbeforeunload = function () {
    return "Are you sure that you want to leave this page?";
}
