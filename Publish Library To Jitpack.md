## Publishing Library

We need to bring our Android project into a public repo on our GitHub account first to continue publishing the library for this tutorial. Build a public repo and push all the files to the repo in our GitHub account.

We can only use this library right now since the library module is only accessible for our project. We’ll have to publish the library on JitPack to make the email-validator library accessible to everyone.

## Building for JitPack
-  Add the JitPack maven repository to the list of repositories in the root-level build.gradle

```gradle
allprojects{
  repositories{
    //..
    maven{ url 'https://jitpack.io' }
  }
}
```
-  Enable maven to publish plugin by adding the following in build.gradle of the library module

```gradle
plugins {
  id 'com.android.library'
  id 'maven-publish'
}
```

-  The code sample below produces a publication for an AAR library’s release. add it to the root level of the build.gradle of the library module.

```gradle
afterEvaluate {
    publishing {
        publications {
            // Creates a Maven publication Called release
            release(MavenPublication) {
                /// Applies the component for the release build variant.
                from components.release

                // You can then customize attributes of the publication as shown below.
                groupId = 'media.uqab'
                artifactId = 'final'
                version = '1.3.60'
            }
        }
    }
}
```

### don't forget to create this `jitpack.yml` file in Packege dir

```yml
jdk:
  - openjdk11
```
otherwise you will get this error during jitpack build

```gradle
* What went wrong:
An exception occurred applying plugin request [id: 'com.android.application']
> Failed to apply plugin 'com.android.internal.application'.
   > Android Gradle plugin requires Java 11 to run. You are currently using Java 1.8.
     You can try some of the following options:
       - changing the IDE settings.
       - changing the JAVA_HOME environment variable.
       - changing `org.gradle.java.home` in `gradle.properties`.
```

## Check Maven Publish Plugin
Let’s check whether all the changes we have done are correctly configured in the maven publish plugin or not. Check that your library can be installed to mavenLocal ($HOME/.m2/repository):
-  Run following command in Android Studio Terminal `./gradlew publishReleasePublicationToMavenLocal`
-  Let’s see the `$HOME/.m2/repository` directory

## Publish Library on JitPack
-  Commit the changes we have done in the library module
-  If everything goes well in the previous step, your library is ready to be released! Create a GitHub release or add a git tag and you’re done!
-  Create a release tag in the GitHub repo
-  Open https://jitpack.io/ and lookup for your repo
-  If there is any error you can see in the “Log” tab with detail like what went wrong.

## For Better Understanding Visit
https://www.talentica.com/blogs/publish-your-android-library-on-jitpack-for-better-reachability/
