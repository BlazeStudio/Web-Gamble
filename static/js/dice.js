$(document).ready(function() {
        $('#lower').click(function() {
            likeButton("lower");
        });

        $('#higher').click(function() {
            likeButton("higher");
        });

        $('#ratio').on('input', function() {
            updateMinMaxValues();
        });

    });

    function likeButton(action) {
        var ratio = document.getElementById("ratio").value;

        $.ajax({
            type: 'GET',
            url: '/bet',
            data: {
                action: action,
                ratio: ratio
            },
            success: function(response) {
                $('#value').text(response.value);
                $('#likeCount').text(response.likes);
                if (response.message.type === "success"){
                    $('#message').removeClass('lost-message').addClass('win-message').text(response.message.text);
                } else {
                    $('#message').removeClass('win-message').addClass('lost-message').text(response.message.text);
                }
            },
            error: function(xhr, status, error) {
                console.error('Error:', error);
            }
        });
    }

    function updateMinMaxValues() {
        var ratio = document.getElementById("ratio").value;
        var max_value = Math.round(999999 * (ratio/100))
        var min_value = Math.round((999999 * (1 - ratio / 100)));

        $('#lower').text('0 - ' + max_value);
        $('#higher').text(min_value + ' - 999999');
    }