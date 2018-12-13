'use strict';

var gulp = require('gulp');
var sass = require('gulp-sass');
var autoprefixer = require('gulp-autoprefixer');

var scssFiles = './resources/sass/agnieszka/*.scss';

gulp.task('sass', function() {
    return gulp.src(scssFiles)
        .pipe(sass().on('error', sass.logError))
        .pipe(autoprefixer({
            browsers: ['last 2 versions'],
            cascade: false
        }))
        .pipe(gulp.dest('./web/home/static/agnieszka/css/'));
});

gulp.task('sass:watch', function() {
    gulp.watch(scssFiles, gulp.series('sass'));
});

gulp.task('copy_bootstrap', function() {
    return gulp.src('./bower_components/bootstrap/dist/**')
        .pipe(gulp.dest('./web/home/static/thirdparty/bootstrap'));
});

gulp.task('copy_bootstrap_sass', function() {
    return gulp.src('./bower_components/bootstrap/scss/**')
        .pipe(gulp.dest('./resources/sass/agnieszka/vendor/bootstrap'));
});

gulp.task('copy_jquery', function() {
    return gulp.src('./bower_components/jquery/dist/**')
        .pipe(gulp.dest('./web/home/static/thirdparty/jquery'));
});

gulp.task('copy_fontawesome', function() {
    return gulp.src('./bower_components/fontawesome/**')
        .pipe(gulp.dest('./web/home/static/thirdparty/fontawesome'));
});

gulp.task('thirdparty', gulp.parallel(
    'copy_bootstrap', 'copy_jquery', 'copy_fontawesome', 'copy_bootstrap_sass'
));
